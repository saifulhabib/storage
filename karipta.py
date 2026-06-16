import telebot
from datetime import datetime

# API Token telah dimasukkan
TOKEN = "8836496309:AAHrP2xncIpE6fQdbB9bLhnCUMNIIPerPW0"
bot = telebot.TeleBot(TOKEN)

# --- Kamus Mini Bausastra ---
kamus_jawa = {
    "asih": "tresna (cinta/kasih sayang)",
    "bagaskara": "srengenge (matahari)",
    "chandra": "rembulan (bulan)",
    "dalu": "wengi (malam)",
    "enjing": "esuk (pagi)",
    "gilir": "ganti (berganti)",
    "harsa": "bungah (gembira)",
    "kalbu": "ati (hati/perasaan)",
    "luhur": "dhuwur (tinggi/mulia)",
    "nembang": "nyanyi (bernyanyi)",
    "rahayu": "slamet (selamat/damai)",
    "sugeng": "slamet (selamat)",
    "tresna": "cinta (cinta)"
}

# --- 1. Sambutan Sugeng Rawuh ---
@bot.message_handler(content_types=['new_chat_members'])
def sugeng_rawuh(message):
    for new_member in message.new_chat_members:
        nama = new_member.first_name
        teks_sambutan = (
            f"ꦱꦸꦒꦼꦁꦫꦮꦸꦃ\n\n"
            f"Sugeng rawuh kisanak *{nama}* ing paguyuban Geguritan Jawa. 🙏\n\n"
            f"Mugi-mugi saged pitepangan, ngangsu kawruh, lan sesarengan ngleluri budaya Jawi ing mriki. "
            f"Ketik /panduan kangge mirsani pitulung bot."
        )
        bot.reply_to(message, teks_sambutan, parse_mode='Markdown')

# --- 2. Mugi Pinanggih Malih ---
@bot.message_handler(content_types=['left_chat_member'])
def mugi_pinanggih_malih(message):
    nama = message.left_chat_member.first_name
    teks_pamit = f"Mugi pinanggih malih, *{nama}*. Rahayu ingkang samya pinanggih. 🍂"
    bot.reply_to(message, teks_pamit, parse_mode='Markdown')

# --- Menu Panduan ---
@bot.message_handler(commands=['start', 'panduan'])
def menu_panduan(message):
    panduan = """
📜 *PANDUAN BOT GEGURITAN* 📜

Sumangga dipun-ginakaken printah ing handap punika:
/weton [DD-MM-YYYY] - Madosi dinten lan pasaran kalender Jawa.
/bausastra [tembung] - Pados tegesipun tembung Jawa.
/panduan - Mirsani menu punika.
"""
    bot.reply_to(message, panduan, parse_mode='Markdown')

# --- 3. Kalender Jawa dan Weton ---
@bot.message_handler(commands=['weton'])
def cek_weton(message):
    try:
        input_tanggal = message.text.split(' ')[1]
        tanggal_cek = datetime.strptime(input_tanggal, "%d-%m-%Y").date()
        
        nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
        nama_pasaran = ["Pahing", "Pon", "Wage", "Kliwon", "Legi"]
        
        patokan_tanggal = datetime.strptime("01-01-2024", "%d-%m-%Y").date()
        selisih_hari = (tanggal_cek - patokan_tanggal).days
        
        indeks_hari = tanggal_cek.weekday()
        indeks_pasaran = selisih_hari % 5
        
        hari = nama_hari[indeks_hari]
        pasaran = nama_pasaran[indeks_pasaran]
        
        bot.reply_to(message, f"Tanggal *{input_tanggal}* dhawah ing:\n✨ *{hari} {pasaran}* ✨", parse_mode='Markdown')
    except:
        bot.reply_to(message, "Format lepat. Cobi: `/weton DD-MM-YYYY`", parse_mode='Markdown')

# --- 4. Bausastra ---
@bot.message_handler(commands=['bausastra'])
def cari_bausastra(message):
    try:
        kata = message.text.split(' ')[1].lower()
        if kata in kamus_jawa:
            bot.reply_to(message, f"📖 *Bausastra*\nTegesipun *{kata.capitalize()}*: {kamus_jawa[kata]}", parse_mode='Markdown')
        else:
            bot.reply_to(message, "Nyuwun pangapunten, tembung dereng kapanggih.", parse_mode='Markdown')
    except:
        bot.reply_to(message, "Cobi: `/bausastra [tembung]`", parse_mode='Markdown')

bot.infinity_polling()
