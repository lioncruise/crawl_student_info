# coding: utf-8

import scrapy
from sqlalchemy import Column, Integer, String, TEXT, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('mysql://root:admin@localhost:3306/test')
DBSession = sessionmaker(bind=engine)


class StudentInfoSpider(scrapy.Spider):
    name = 'student_info_spider'
    base_url = 'http://xueji.ucas.ac.cn/record/iframeB1?id='
    start_urls = [base_url + str(i) for i in range(358612, 408200)]

    def parse(self, response):
        name = response.css('td.a152')[0].css('td ::text').extract_first()  # name
        birthday = response.css('td.a171')[0].css('td ::text').extract_first()  # birthday
        school = response.css('td.a137')[0].css('td ::text').extract_first()  # school
        institute = response.css('td.a141')[0].css('td ::text').extract_first()  # institute
        id_no = response.css('td.a143')[0].css('td ::text').extract_first()  # id
        address = response.css('td.a123')[0].css('td ::text').extract_first()  # address
        hometown = response.css('td.a130')[0].css('td ::text').extract_first()  # jiguan
        student_no = response.css('td.a150')[0].css('td ::text').extract_first()  # school_id
        avatar_url = response.css('div.a157 > img ::attr(src)').extract_first()  # xueji_url
        phone = response.css('td.a130')[1].css('td ::text').extract_first()  # phone
        degree = response.css('td.a27')[0].css('td ::text').extract_first()  # xuewei
        gender = response.css('td.a146')[0].css('td ::text').extract_first()  # gender
        family = response.css('td.a54')[0].css('td ::text').extract_first()  # family

        session = DBSession()
        new_user = Student(name=name, birthday=birthday, school=school, institute=institute, id_no=id_no,
                           address=address, hometown=hometown, student_no=student_no, avatar_url=avatar_url,
                           phone=phone, degree=degree, gender=gender, family=family)
        session.add(new_user)
        session.commit()
        session.close()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    birthday = Column(String(255))
    school = Column(String(255))
    institute = Column(String(255))
    id_no = Column(String(255))
    address = Column(String(255))
    hometown = Column(String(255))
    student_no = Column(String(255))
    avatar_url = Column(String(255))
    phone = Column(String(255))
    degree = Column(String(255))
    gender = Column(String(255))
    family = Column(TEXT)
