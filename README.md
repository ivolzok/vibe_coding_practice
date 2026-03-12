# ASCII Art Generator (Pillow)

Python-скрипт, который принимает изображение, переводит его в чёрно-белое, масштабирует до **100×50** и печатает ASCII-арт в консоль, используя набор символов:

`@%#*+=-:. `

## Требования

- Python 3.9+
- Pillow

Установка Pillow:

```bash
python -m pip install pillow
```

## Запуск

```bash
python main.py path/to/image.png
```

Пример для Windows (PowerShell):

```bash
python main.py "C:\path\to\image.jpg"
```

## Как это работает

- Конвертация в grayscale (`L`)
- Масштабирование до **100×50**
- Маппинг яркости пикселей \(0..255\) в символы ASCII (чем темнее пиксель, тем “плотнее” символ)