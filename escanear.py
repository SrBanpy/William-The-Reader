import easyocr
def escanear_ocr(imagen):
    escaneo = easyocr.Reader(['en', 'es', 'fr', 'de', 'it', 'pt', 'nl', 'vi', 'id', 'tr', 'pl', 'sv', 'cs', 'da', 'no', 'hu', 'ro', 'sk', 'hr', 'sl', 'et', 'lt', 'lv', 'sq', 'sw', 'cy', 'ga', 'is'], gpu=False)


    resultados = escaneo.readtext(imagen)
    texto_escaneado = ''
    for resultado in resultados:
        texto_escaneado+= resultado[1] + '\n'

    return texto_escaneado

