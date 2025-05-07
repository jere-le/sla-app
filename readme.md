# Azure SLA -laskuri

Tämä on yksinkertainen mutta tehokas Streamlit-pohjainen web-sovellus, jolla voit laskea yhdistetyn SLA-prosentin valitsemillesi Azure-palveluille.

## 🔧 Toiminnot

- Valitse Azure-palvelut valikosta
- Sovellus hakee viralliset SLA-prosentit tiedostosta `azure_sla_reference.txt`
- Näet yhdistetyn SLA:n ja arvioidun kuukausikatkon (minuuteissa)

## 📦 Asennus

1. Luo virtuaaliympäristö ja aktivoi se:

```bash
python3 -m venv venv
source venv/bin/activate

2.	Asenna riippuvuudet
