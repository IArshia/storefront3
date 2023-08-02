from django.core.exceptions import ValidationError


def validate_file_size(file):
    mx_size_kb = 50

    if file.size > mx_size_kb * 1024:
        raise ValidationError(f'File cannot be larger than{mx_size_kb}KB!')
       
    