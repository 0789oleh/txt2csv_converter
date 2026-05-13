import os
import csv
from pathlib import Path
import typer
from typing import Optional
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

app = typer.Typer(help="Утилита для конвертации TXT (TSV) в CSV")
__version__ = "0.1.0"


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
        
        try:
            with open(input_file, 'r', encoding='utf-8') as in_file:
                # Читаем строки, убираем пустые
                lines = []
                for line in in_file:
                    clean_line = line.strip()
                    if not clean_line:
                        continue
                
                    # split() без параметров разделит и по табу, и по 10 пробелам сразу
                    columns = clean_line.split() 
                    lines.append(columns)
            
                with open(output_file, 'w', newline='', encoding='utf-8') as out_file:
                    writer = csv.writer(out_file)
                    writer.writerows(lines)
        
            typer.secho(f"Успешно обработано строк: {len(lines)}", fg=typer.colors.GREEN)
            
        except Exception as e:
            typer.secho(f"❌ Ошибка: {e}", fg=typer.colors.RED, err=True)
            raise typer.Exit(1)
    

if __name__ == "__main__":
    app()
