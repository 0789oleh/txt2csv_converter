class ConversionError(Exception):
    """Базовая ошибка конвертации."""
    pass


class ParsingError(Exception):
    pass


class MetadataError(Exception):
    """Should be raised after metadata handling implementation"""
    pass


class ValidationError(Exception):
    pass
