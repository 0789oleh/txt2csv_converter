import os
import csv
from pathlib import Path
import typer
from typing import Optional
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from  utils import process_text_lines, normalize_numeric_value


app = typer.Typer(help="Утилита для конвертации TXT (TSV) в CSV")
__version__ = "0.2.0"


def version_callback(value: bool):
    if value:
        typer.echo(f"TXT2CSV Converter Version: {__version__}")
        raise typer.Exit()


@app.command()
def convert(
    input_file: Path = typer.Argument(
        ..., 
        exists=True, 
        readable=True, 
        help="Путь к исходному текстовому файлу"
    ),
    output_file: Path = typer.Argument(
        ..., 
        writable=True, 
        help="Путь для сохранения CSV файла"
    ),
    delimiter: str = typer.Option(
        "\t", 
        "--delimiter", "-d", 
        help="Разделитель в исходном файле"
    ),
    quotechar: str = typer.Option(
        '"', 
        "--quote", "-q", 
        help="Символ кавычек для CSV"
    ),
    version: Optional[bool] = typer.Option(
        None, 
        "--version", 
        "-v",
        callback=version_callback,
        is_eager=True,  # Выполнить немедленно, игнорируя другие ошибки аргументов
        help="Показать версию программы и выйти"
    ),
    preview: Optional[bool] = typer.Option(
        None, 
        "--preview",
        "-p",
        help="Режим превью"
    ), 
    encoding: Optional[str] = typer.Option(
        None, 
        "--encoding",
        "-e", 
        help="Encoding (default uff-8)"
    )   
):
    """Конвертирует TXT в CSV с индикацией прогресса."""
    
    # Получаем размер файла для прогресс-бара
    file_size = os.path.getsize(input_file)
    
    # Настраиваем внешний вид бара
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        transient=True, # Бар исчезнет после завершения работы
    ) as progress:
        
        task = progress.add_task(description="Конвертация...", total=file_size)
        if not encoding:
            encoding='utf-8'

        try:
            # 1. Чтение данных
            with open(input_file, 'r', encoding=encoding) as in_file:
                raw_lines = in_file.readlines()
            
            # 2. Обработка через изолированный модуль
            processed_data = process_text_lines(raw_lines)
            
            # 3. Режим превью
            if preview:
                progress.stop()
                preview_data = process_text_lines(raw_lines, limit=5)
                typer.secho("\n✨ [Preview] Первые 5 строк:", fg=typer.colors.CYAN, bold=True)
                for row in preview_data:
                    typer.echo(" | ".join(row))
                typer.echo('')
                
                confirm = typer.confirm("Данные распознаны корректно? Записать в итоговый CSV?")
                
                # Если пользователь ввел не 'y' и не 'yes' (или просто нажал Enter)
                if not confirm:
                    typer.secho("❌ Конвертация отменена пользователем. Файл НЕ сохранен.", fg=typer.colors.YELLOW)
                    raise typer.Exit()
            
                typer.secho("🚀 Продолжаем запись...", fg=typer.colors.GREEN)

            
            # 4. Запись результата
            with open(output_file, 'w', newline='', encoding='utf-8') as out_file:
                writer = csv.writer(out_file)
                writer.writerows(processed_data)
            
            typer.secho(f"Успешно обработано строк: {len(processed_data)}", fg=typer.colors.GREEN)
        
        except FileNotFoundError:
            typer.echo(f"❌ Ошибка: Файл '{input_file}' не найден.", fg=typer.colors.RED, err=True)
            raise typer.Exit(code=1)
    

if __name__ == "__main__":
    app()
