import psycopg2
import psycopg2.extras
from flask import Flask,redirect,url_for,render_template,request,flash
from flask_cors import CORS
connection = psycopg2.connect("dbname=liman user=postgres password=u8yi8a1-")
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/a')
def Index():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM konteyner"
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template('konteyner.html', list_users = list_users)

@app.route("/add_konteyner",methods=['POST'])
def add_konteyner():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        TÜR = request.form['TÜR']
        AGIRLIK= request.form['AGIRLIK']
        GEMİNO= request.form['GEMİNO']
        cur.execute(''' INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO)  VALUES (%s,%s,%s)''', (TÜR,AGIRLIK,GEMİNO))
        connection.commit()
        if(int(AGIRLIK)>=0 and TÜR!='kimyasal'):
            flash('Gemiye yük başarıyla eklendi.')
        elif(int(AGIRLIK)<0 and TÜR!='kimyasal'):
            flash('Hata 0 dan az agırlık eklenemez')
        elif(TÜR=='kimyasal'):
            flash('Kimyasal konteyner gemiye yüklenemez')
        return redirect(url_for('Index'))


@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_konteyner(id):
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM konteyner WHERE KID::int= {0}'.format(id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('editkonteyner.html', konteynerr = data[0])

@app.route('/update_konteyner/<id>', methods=['POST','GET'])
def update_konteyner(id):
    if request.method == 'POST':
        TÜR = request.form['TÜR']
        AGIRLIK= request.form['AGIRLIK']
        GEMİNO= request.form['GEMİNO']
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cur.execute("""
            UPDATE konteyner
            SET TÜR = {0},
                AGIRLIK = {1},
                GEMİNO = {2}
            WHERE KID = %s
        """.format(TÜR, AGIRLIK, GEMİNO, id))
        flash('Konteyner başarıyla güncellendi.')
        conn.commit()
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_konteyner(id):
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("DELETE FROM konteyner WHERE KID::int ={0}".format(id))
    connection.commit()
    flash('Konteyner başarıyla silindi.')
    return redirect(url_for('Index'))

@app.route('/gemi/<name>')
def Index1(name):
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = " SELECT konteyner.KID,konteyner.TÜR,konteyner.AGIRLIK,konteyner.GEMİNO FROM konteyner, gemi WHERE konteyner.GEMİNO=gemi.GEMİNO AND gemi.GEMİAD ='{0}'".format(name)
    cur.execute(s)
    listt = cur.fetchall()
    return render_template('sorgu.html', listt = listt)


@app.route("/gemi_konteyner",methods=['POST'])
def gemi_konteyner():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        GEMİAD = request.form['GEMİAD']
        cur.execute(" SELECT konteyner.KID,konteyner.TÜR,konteyner.AGIRLIK,konteyner.GEMİNO FROM konteyner, gemi WHERE konteyner.GEMİNO=gemi.GEMİNO AND gemi.GEMİAD ='{0}'".format(GEMİAD))
        connection.commit()
        return redirect(url_for('Index1',name =GEMİAD))

@app.route('/view')
def create_view():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = " CREATE VIEW kaptan AS SELECT * FROM calisan WHERE UNVAN='Kaptan' ; SELECT * FROM kaptan"
    cur.execute(s)
    listv = cur.fetchall()
    return render_template('view.html', listv = listv)

@app.route('/kadın')
def create_kadın():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT * FROM calisan WHERE CINSIYET='K' INTERSECT SELECT * FROM calisan WHERE UNVAN<>'Kaptan'"
    cur.execute(s)
    listv = cur.fetchall()
    return render_template('kadın.html', listv = listv)

@app.route('/unvan')
def create_unvan():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "SELECT UNVAN,avg(MAAS) FROM calisan GROUP BY UNVAN HAVING COUNT(*)>1 "
    cur.execute(s)
    listu = cur.fetchall()
    return render_template('unvan.html', listu = listu)

@app.route('/func1/<name>')
def Index2(name):
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = '''CREATE TYPE gemiyuk AS (GEMİNO varchar(25), YUK INT);
                   CREATE OR REPLACE FUNCTION yuk (name1 varchar(25))
                    RETURNS gemiyuk AS $$
                    DECLARE
                    cursor1 CURSOR FOR SELECT AGIRLIK FROM gemi,konteyner WHERE gemi.GEMİNO=konteyner.GEMİNO AND GEMİAD=name1;
                    total INT;
                    last gemiyuk;
                    BEGIN
                       total:=0;
                       FOR gemi_rec IN cursor1 LOOP
                          total=total+gemi_rec.AGIRLIK;
                        END LOOP;
                        last:=(name1,total);
                     RETURN last;
                    END;
                    $$ LANGUAGE 'plpgsql';
                    SELECT yuk('name')    '''
    cur.execute(s)
    listf = cur.fetchall()
    return render_template('FUNC1.html', listf = listf)


@app.route("/gemi_yuk",methods=['POST'])
def gemi_yuk():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        GEMİAD = request.form['GEMİAD1']
        return redirect(url_for('Index2',name=GEMİAD))



@app.route('/func2/<name>')
def Index3(name):
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = '''CREATE TYPE gemihacim AS (GEMİNO varchar(25), hacim INT);
                   CREATE OR REPLACE FUNCTION hacim (name1 varchar(25))
                    RETURNS gemihacim AS $$
                    DECLARE
                    cursor2 CURSOR FOR SELECT UZUNLUK,GENISLIK FROM gemi WHERE GEMİAD=name1;
                    total1 INT;
                    last1 gemihacim;
                    BEGIN
                       total1:=1;
                       FOR gemi_rec IN cursor2 LOOP
                          total1=total1*gemi_rec.UZUNLUK*gemi_rec.GENISLIK;
                        END LOOP;
                        last1:=(name1,total1);
                     RETURN last1;
                    END;
                    $$ LANGUAGE 'plpgsql';
                    SELECT hacim('name')    '''
    cur.execute(s)
    listf = cur.fetchall()
    return render_template('FUNC2.html', listf = listf)


@app.route("/gemi_hacim",methods=['POST'])
def gemi_hacim():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        GEMİAD = request.form['GEMİAD2']
        return redirect(url_for('Index3',name=GEMİAD))
@app.route('/func3/<unvan1>')
def Index4(unvan1):
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = '''CREATE TYPE cinsiyet AS (unvan varchar(25), kadın INT,erkek INT);
                   CREATE OR REPLACE FUNCTION unvanc (unvann varchar(25))
                    RETURNS cinsiyet AS $$
                    DECLARE
                    cursor3 CURSOR FOR SELECT CINSIYET FROM calisan WHERE UNVAN=unvann;
                    KADIN1 INT;
                    ERKEK1 INT;
                    last2 cinsiyet;
                    BEGIN
                       KADIN1 :=0;
                       ERKEK1 :=0;
                       FOR calisani_rec IN cursor3 LOOP
                          IF calisani_rec.CINSIYET='K' THEN
                           KADIN1:=KADIN1+1;
                          ELSE
                           ERKEK1:=ERKEK1+1 ;
                          END IF;
                        END LOOP;
                        last2:=(unvann,KADIN1,ERKEK1);
                     RETURN last2;
                    END;
                    $$ LANGUAGE 'plpgsql';
                    SELECT unvanc('unvan1')    '''
    cur.execute(s)
    listc = cur.fetchall()
    return render_template('FUNC3.html', listc = listc)
@app.route("/calisan_cinsiyet",methods=['POST'])
def calisan_cinsiyet():
    cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        UNVAN1 = request.form['UNVAN']
        return redirect(url_for('Index4',unvan1=UNVAN1))

if __name__ == "__main__":
    app.run(debug=True)
