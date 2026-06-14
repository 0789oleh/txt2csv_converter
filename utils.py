import re
from typing import List


def normalize_numeric_value(val: str) -> str:
    """
    Заменяет запятую на точку, ТОЛЬКО если запятая стоит между двумя цифрами.
    Пример: '0,2345' -> '0.2345', '3,14e-01' -> '3.14e-01'
    Но текст 'Иваново, ул. Ленина' останется без изменений.
    """
    # (?<=\d) — сзади должна быть цифра
    # , — сама запятая
    # (?=\d) — впереди должна быть цифра
    return re.sub(r'(?<=\d),(?=\d)', '.', val)


def process_text_lines(raw_lines: List[str], limit: int = None) -> List[List[str]]:
    """
    Парсит строки, убирает пустые и нормализует числа.
    Если передан limit, обрабатывает только указанное количество строк.
    """
    processed_data = []
    
    # Берем срез, если лимит задан
    lines_to_process = raw_lines[:limit] if limit else raw_lines
    
    for line in lines_to_process:
        clean_line = line.strip()
        if not clean_line:
            continue
            
        columns = clean_line.split()
        normalized_columns = [normalize_numeric_value(cell) for cell in columns]
        processed_data.append(normalized_columns)
        
    return processed_data