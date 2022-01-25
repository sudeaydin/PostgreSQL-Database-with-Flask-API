import psycopg2
from psycopg2 import Error
connection = psycopg2.connect("dbname=liman user=postgres password=u8yi8a1-")
try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="u8yi8a1-",
                                  host="localhost",
                                  port="5432",
                                  database="liman")


    cursor = connection.cursor()
    create_table_query = '''CREATE TABLE gemi
          (GEMİNO VARCHAR(25) PRIMARY KEY     NOT NULL,
           GEMİAD VARCHAR(25)    NOT NULL,
           KAPTANID VARCHAR(25),
           MAXYUK INT,
           UZUNLUK INT,
           GENISLIK INT); '''

    cursor.execute(create_table_query)
    connection.commit()

    create_table_query1 = '''CREATE TABLE calisan
          (ID VARCHAR(25) PRIMARY KEY     NOT NULL,
           AD VARCHAR(25)    NOT NULL,
           SOYAD VARCHAR(25)    NOT NULL,
           MAAS INT,
           UNVAN VARCHAR(25),
           ADRESS VARCHAR(25),
           DOGUM VARCHAR(25),
           CINSIYET VARCHAR(25),
           GEMİNO VARCHAR(25)); '''

    cursor.execute(create_table_query1)
    connection.commit()

    create_table_query2 = '''
          CREATE SEQUENCE seq MINVALUE 1000 MAXVALUE 9999 INCREMENT BY 1 ;
          CREATE TABLE konteyner
          (KID VARCHAR(25) DEFAULT nextval('seq') NOT NULL,
           TÜR VARCHAR(25) not null  ,
           AGIRLIK INT,
           GEMİNO VARCHAR(25) not null,
           PRIMARY KEY(KID)); '''

    cursor.execute(create_table_query2)
    connection.commit()

    create_table_query3 = '''CREATE TABLE iskele
          (ISKELENO VARCHAR(25) PRIMARY KEY     NOT NULL,
           GENISLIK INT  ,
           UZUNLUK INT,
           GEMİNO VARCHAR(25)); '''

    cursor.execute(create_table_query3)
    connection.commit()



    tgfunc=''' CREATE OR REPLACE FUNCTION tg1()
               RETURNS TRIGGER AS $$
               BEGIN
                 IF (new.AGIRLIK<0) THEN
                   RAISE NOTICE 'YÜKÜN AGIRLIĞI 0 DAN KÜÇÜK OLAMAZ';
                   RETURN NULL;
                 ELSE
                   RETURN NEW;
                 END IF;
               END;
               $$ LANGUAGE 'plpgsql';'''

    cursor.execute(tgfunc)
    connection.commit()
    create_trigger=''' CREATE TRIGGER agırlık
                               BEFORE INSERT
                               ON konteyner
                               FOR EACH ROW EXECUTE PROCEDURE tg1()'''
    cursor.execute(create_trigger)
    connection.commit()

    tgfunc1=''' CREATE OR REPLACE FUNCTION tg2()
               RETURNS TRIGGER AS $$
               BEGIN
                 IF (new.TÜR='kimyasal') THEN
                   RAISE NOTICE 'kimyasal konteyner eklenemez.';
                   RETURN NULL;
                 ELSE
                   RETURN NEW;
                 END IF;
               END;
               $$ LANGUAGE 'plpgsql';'''

    cursor.execute(tgfunc1)
    connection.commit()
    create_trigger1=''' CREATE TRIGGER kimyasal
                               BEFORE INSERT
                               ON konteyner
                               FOR EACH ROW EXECUTE PROCEDURE tg2()'''
    cursor.execute(create_trigger1)
    connection.commit()











    insert1="""INSERT INTO gemi VALUES ('12345','yıldız','123',3,40,5)"""
    cursor.execute(insert1)
    connection.commit()
    insert2="""INSERT INTO gemi VALUES ('23456','Kara İnci','234',6,50,7)"""
    cursor.execute(insert2)
    connection.commit()
    insert3="""INSERT INTO gemi VALUES ('34567','nusret','345',45,150,30)"""
    cursor.execute(insert3)
    connection.commit()
    insert4="""INSERT INTO gemi VALUES ('45678','ay','456',8,80,10)"""
    cursor.execute(insert4)
    connection.commit()
    insert5="""INSERT INTO gemi VALUES ('56789','bulut','567',440,380,100)"""
    cursor.execute(insert5)
    connection.commit()
    insert6="""INSERT INTO gemi VALUES ('67890','Marco Polo','678',500,396,54)"""
    cursor.execute(insert6)
    connection.commit()
    insert7="""INSERT INTO gemi VALUES ('78901','Vale Max','789',300,400,100)"""
    cursor.execute(insert7)
    connection.commit()
    insert8="""INSERT INTO gemi VALUES ('89012','Kızım Kuzum','890',56,30,10)"""
    cursor.execute(insert8)
    connection.commit()
    insert9="""INSERT INTO gemi VALUES ('90123','Uçan Hollandalı','901',100,200,50)"""
    cursor.execute(insert9)
    connection.commit()
    insert10="""INSERT INTO gemi VALUES ('01234','Mavi Balina','012',150,300,55)"""
    cursor.execute(insert10)
    connection.commit()


    insert11="""INSERT INTO calisan VALUES ('123','Alper Teoman','Kolik',100000,'Kaptan','pendik','01.01.2000','E','12345')"""
    cursor.execute(insert11)
    connection.commit()
    insert12="""INSERT INTO calisan VALUES ('234','Sude Şevval','Aydın',100000,'Kaptan','sancaktepe','20.01.2001','K','23456')"""
    cursor.execute(insert12)
    connection.commit()
    insert13="""INSERT INTO calisan VALUES ('345','Kemal','Selçuk',100000,'Kaptan','beylikdüzü','23.10.2000','E','34567')"""
    cursor.execute(insert13)
    connection.commit()
    insert14="""INSERT INTO calisan VALUES ('456','Arda','Taş',100000,'Kaptan','ataşehir','18.02.2001','E','45678')"""
    cursor.execute(insert14)
    connection.commit()
    insert15="""INSERT INTO calisan VALUES ('567','Ahmet','Yılmaz',100000,'Kaptan','maltepe','24.09.1989','E','56789')"""
    cursor.execute(insert15)
    connection.commit()
    insert16="""INSERT INTO calisan VALUES ('678','İbrahim','Tatlıses',10000,'Kaptan','şanlıurfa','01.01.1950','E','67890')"""
    cursor.execute(insert16)
    connection.commit()
    insert17="""INSERT INTO calisan VALUES ('789','Furkan','Çakmak',100000,'Kaptan','trabzon','09.01.1981','E','78901')"""
    cursor.execute(insert17)
    connection.commit()
    insert18="""INSERT INTO calisan VALUES ('890','Selin','Tipi',100000,'Kaptan','kadıköy','21.06.2001','K','89012')"""
    cursor.execute(insert18)
    connection.commit()
    insert19="""INSERT INTO calisan VALUES ('901','Mahmut','Tuncer',100000,'Kaptan','şanlıurfa','01.01.1951','E','90123')"""
    cursor.execute(insert19)
    connection.commit()
    insert20="""INSERT INTO calisan VALUES ('012','Buse','Yalaz',100000,'Kaptan','kartal','06.09.1999','K','01234')"""
    cursor.execute(insert20)
    connection.commit()
    insert21="""INSERT INTO calisan VALUES ('098','Vedat','Milör',5000,'Aşçı','kartal','06.09.1969','E','12345')"""
    cursor.execute(insert21)
    connection.commit()
    insert22="""INSERT INTO calisan VALUES ('987','Berke','Kılıç',7000,'Makinist','maltepe','09.02.1998','E','89012')"""
    cursor.execute(insert22)
    connection.commit()
    insert23="""INSERT INTO calisan VALUES ('876','Harry','Styles',10000,'Çarkçıbaşı','londra','02.02.1994','E','23456')"""
    cursor.execute(insert23)
    connection.commit()
    insert24="""INSERT INTO calisan VALUES ('765','Margot','Robbie',5000,'Stajer','las vegas','06.09.1989','K','12345')"""
    cursor.execute(insert24)
    connection.commit()
    insert25="""INSERT INTO calisan VALUES ('654','Serdar','Ortaç',20000,'Stajer','kastamonu','05.09.1979','E','89012')"""
    cursor.execute(insert25)
    connection.commit()
    insert26="""INSERT INTO calisan VALUES ('543','Thor','Odinson',100000,'Çarkçıbaşı','asgard','06.10.1989','E','23456')"""
    cursor.execute(insert26)
    connection.commit()

    insert27="""INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO) VALUES ('sağlık',10,'12345')"""
    cursor.execute(insert27)
    connection.commit()
    insert28="""INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO) VALUES ('gıda',100,'23456')"""
    cursor.execute(insert28)
    connection.commit()
    insert29="""INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO) VALUES ('tekstil',15,'34567')"""
    cursor.execute(insert29)
    connection.commit()
    insert30="""INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO) VALUES ('yakıt',30,'45678')"""
    cursor.execute(insert30)
    connection.commit()
    insert31="""INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO) VALUES ('yakıt',25,'56789')"""
    cursor.execute(insert31)
    connection.commit()
    insert32="""INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO) VALUES ('gıda',20,'67890')"""
    cursor.execute(insert32)
    connection.commit()
    insert33="""INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO) VALUES ('sağlık',69,'78901')"""
    cursor.execute(insert33)
    connection.commit()
    insert34="""INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO) VALUES ('yakıt',150,'89012')"""
    cursor.execute(insert34)
    connection.commit()
    insert35="""INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO) VALUES ('tekstil',10,'90123')"""
    cursor.execute(insert35)
    connection.commit()
    insert36="""INSERT INTO konteyner(TÜR,AGIRLIK,GEMİNO) VALUES ('sağlık',100,'01234')"""
    cursor.execute(insert36)
    connection.commit()


    insert37="""INSERT INTO iskele VALUES ('00',100,30,'12345')"""
    cursor.execute(insert37)
    connection.commit()
    insert38="""INSERT INTO iskele VALUES ('01',100,30,'23456')"""
    cursor.execute(insert38)
    connection.commit()
    insert39="""INSERT INTO iskele VALUES ('02',100,20,'34567')"""
    cursor.execute(insert39)
    connection.commit()
    insert40="""INSERT INTO iskele VALUES ('03',400,200,'45678')"""
    cursor.execute(insert40)
    connection.commit()
    insert41="""INSERT INTO iskele VALUES ('04',400,200,'56789')"""
    cursor.execute(insert41)
    connection.commit()
    insert43="""INSERT INTO iskele VALUES ('05',400,200,'67890')"""
    cursor.execute(insert43)
    connection.commit()
    insert44="""INSERT INTO iskele VALUES ('06',100,50,'78901')"""
    cursor.execute(insert44)
    connection.commit()
    insert45="""INSERT INTO iskele VALUES ('07',200,100,'89012')"""
    cursor.execute(insert45)
    connection.commit()
    insert46="""INSERT INTO iskele VALUES ('08',400,200,'90123')"""
    cursor.execute(insert46)
    connection.commit()
    insert47="""INSERT INTO iskele VALUES ('09',400,200,'01234')"""
    cursor.execute(insert47)
    connection.commit()

    cons1="ALTER TABLE calisan ADD CONSTRAINT fk1 FOREIGN KEY(GEMİNO) REFERENCES gemi(GEMİNO) ON DELETE CASCADE"
    cursor.execute(cons1)
    connection.commit()
    cons2="ALTER TABLE gemi ADD CONSTRAINT fk FOREIGN KEY(KAPTANID) REFERENCES calisan(ID) ON DELETE CASCADE"
    cursor.execute(cons2)
    connection.commit()
    cons3="ALTER TABLE konteyner ADD CONSTRAINT fk2 FOREIGN KEY(GEMİNO) REFERENCES gemi(GEMİNO) ON DELETE CASCADE"
    cursor.execute(cons3)
    connection.commit()
    cons4="ALTER TABLE iskele ADD CONSTRAINT fk3 FOREIGN KEY(GEMİNO) REFERENCES gemi(GEMİNO) ON DELETE CASCADE"
    cursor.execute(cons4)
    connection.commit()
    cons5="ALTER TABLE calisan ADD CONSTRAINT asgari CHECK(MAAS>4000)"
    cursor.execute(cons5)
    connection.commit()
    cons6="ALTER TABLE gemi ADD CONSTRAINT maxlenght CHECK(UZUNLUK<401)"
    cursor.execute(cons6)
    connection.commit()
















    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
