def generate_product_code(type):
    from datetime import datetime
    time_data = datetime.now()
    date_time_str = time_data.strftime("%Y%m%d%H%M%S")
    switcher = {
        'complement': 'CMP',
        'burger': 'BRG',
        'menu': 'MNU',
        'commande': 'ORD',
        'payment': 'PYM',
        'invoice': 'INV',
        'user': 'USR',
        'image': 'IMG',
        'gestionnaire': 'GST'
    }
    code = switcher.get(type, "Invalid type")
    if code == 'Invalid type':
        return None
    return code+''+date_time_str