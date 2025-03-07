from flask import Flask, render_template, request, url_for, redirect, flash
import mysql.connector

app = Flask(__name__, static_folder='static')
app.secret_key = "your_secret_key"  # Flash mesajlar için gerekli

# MySQL veritabanı bağlantısı
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Veritabanı adresi
        user="root",       # Kullanıcı adı
        password="mrs_smrSeher12",  # Şifre
        database="anime_db"         # Veritabanı adı
    )

# Ana sayfa: Posterleri listeler
@app.route('/')
def main_page():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, title, poster FROM anime")
    animes = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('main_page.html', animes=animes)

# Content sayfası: Seçilen filmin bilgilerini gösterir
@app.route('/content')
def content_page():
    anime_id = request.args.get('id')
    if not anime_id:
        return "ID belirtilmedi!", 400
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM anime WHERE id = %s", (anime_id,))
    anime = cursor.fetchone()
    cursor.close()
    connection.close()
    if anime is None:
        return "Anime bulunamadı!", 404
    return render_template('content.html', anime=anime)

# Profil sayfası: Kullanıcı kaydı
@app.route('/profile', methods=['GET', 'POST'])
def profile_page():
    error_message = None
    success_message = None

    if request.method == 'POST':
        # Registration logic
        if 'register' in request.form:
            first_name = request.form.get('first-name', '').strip()
            last_name = request.form.get('last-name', '').strip()
            email = request.form.get('email', '').strip()
            password = request.form.get('password', '').strip()
            confirm_password = request.form.get('confirm-password', '').strip()
            gender = ', '.join(request.form.getlist('gender'))
            animation_pref = request.form.get('animation', '').strip()
            preferences = request.form.get('preferences', '').strip()

            # Password validation
            if password != confirm_password:
                error_message = 'Şifreler eşleşmiyor!'
            elif not first_name or not last_name or not email or not password:
                error_message = 'Tüm alanları doldurmanız gerekiyor!'
            else:
                try:
                    # Insert into the database
                    connection = get_db_connection()
                    cursor = connection.cursor()
                    cursor.execute("""
                        INSERT INTO users (first_name, last_name, email, password, gender, animation_pref, preferences)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (first_name, last_name, email, password, gender, animation_pref, preferences))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    success_message = 'Kaydınız başarıyla oluşturulmuştur!'
                except mysql.connector.Error as err:
                    error_message = f'Bir hata oluştu: {err}'

        # Login logic
        elif 'login' in request.form:
            email = request.form.get('email', '').strip()
            password = request.form.get('password', '').strip()

            # Validate login credentials
            connection = get_db_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
            user = cursor.fetchone()
            cursor.close()
            connection.close()

            if user:
                flash('Giriş başarılı!', 'success')
                return redirect(url_for('main_page'))  # Redirect to main page if login successful
            else:
                error_message = 'E-posta veya şifre hatalı!'

    return render_template('profile.html', error_message=error_message, success_message=success_message)

# Arama özelliği
@app.route('/search')
def search():
    query = request.args.get('query', '').strip()
    if not query:
        flash("Arama terimi boş olamaz!")
        return redirect(url_for('main_page'))
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id FROM anime WHERE title LIKE %s", (f"%{query}%",))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    if result:
        return redirect(url_for('content_page', id=result['id']))
    else:
        flash("Aranan anime bulunamadı!")
        return redirect(url_for('main_page'))

if __name__ == '__main__':
    app.run(debug=True)
