from extension import db

class Book(db.Model):
    # 这是SQLAlchemy的model类，用于映射数据库中的book表，定义表的结构和字段信息
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_number = db.Column(db.String(255), nullable=False)
    book_name = db.Column(db.String(255), nullable=False)
    book_type = db.Column(db.String(255), nullable=False)
    book_prize = db.Column(db.Float, nullable=False)
    author = db.Column(db.String(255))
    book_publisher = db.Column(db.String(255))

    @staticmethod
    # 这是一个装饰器，用于定义一个静态方法，即不需要实例化类就可以调用的方法。
    def init_db():
        # 这是一个静态方法，用于初始化数据库，往book表中插入一些书籍信息。
        rets = [
            (1, '001', '活着', '小说', 39.9, '余华', 'publisher'),
            (2, '002', '1984', '小说', 29.9, '乔治·奥威尔', 'publisher'),
            (3, '003', '傲慢与偏见', '小说', 35.0, '简·奥斯汀', 'publisher'),
            (4, '004', '百年孤独', '小说', 45.0, '加西亚·马尔克斯', 'publisher'),
            (5, '005', '战争与和平', '小说', 55.0, '列夫·托尔斯泰', 'publisher'),
            (6, '006', '威尼斯商人', '戏剧', 25.0, '威廉·莎士比亚', 'publisher'),
            (7, '007', '麦田里的守望者', '小说', 32.0, 'J.D.塞林格', 'publisher'),
            (8, '008', '红楼梦', '小说', 42.0, '曹雪芹', 'publisher'),
            (9, '009', '罪与罚', '小说', 38.0, '陀思妥耶夫斯基', 'publisher'),
            (10, '010', '飘', '小说', 40.0, '玛格丽特·米切尔', 'publisher'),
            (11, '003', '平凡的世界', '小说', 45.5, '路遥', '北京出版社'),
            (12, '004', '1984', '科幻', 36.7, '乔治·奥威尔', '上海出版社'),
            (13, '005', '围城', '小说', 29.9, '钱钟书', '广州出版社'),
            (14, '006', '流浪地球', '科幻', 25.6, '刘慈欣', '深圳出版社'),
            (15, '007', '白夜行', '悬疑', 33.8, '东野圭吾', '东京出版社'),
            (16, '008', '红楼梦', '小说', 55.0, '曹雪芹', '南京出版社'),
            (17, '009', '时间机器', '科幻', 21.3, '赫伯特·乔治·威尔斯', '伦敦出版社'),
            (18, '010', '解密', '悬疑', 28.4, '丹·布朗', '纽约出版社'),
            (19, '011', '挪威的森林', '小说', 36.9, '村上春树', '东京出版社'),
            (20, '012', '全球通史', '历史', 49.5, '约翰·罗伯茨', '伦敦出版社'),
            (21, '013', '三体Ⅱ', '科幻', 89.5, '刘慈欣', '重庆出版社'),
            (22, '014', '嫌疑人X的献身', '悬疑', 27.8, '东野圭吾', '东京出版社'),
            (23, '015', '百年孤独', '小说', 42.3, '加西亚·马尔克斯', '墨西哥城出版社'),
            (24, '016', '银河帝国', '科幻', 18.9, '艾萨克·阿西莫夫', '纽约出版社')
        ]
        # rets = [...]: 这是一个包含书籍信息的列表，每个元素是一个元组，包含了书籍的
        # id、编号、名称、类型、价格、作者和出版商等信息。
        for ret in rets:
            book = Book()
            book.id = ret[0]
            book.book_number = ret[1]
            book.book_name = ret[2]
            book.book_type = ret[3]
            book.book_prize = ret[4]
            book.author = ret[5]
            book.book_publisher = ret[6]
            db.session.add(book)
        db.session.commit()
        # for ret in rets: :遍历书籍信息列表。
        # book = Book(): 创建一个Book对象。
        # book.id = ret[0]: 设置Book对象的id属性为元组中的第一个元素。
        # db.session.add(book): 将Book对象添加到数据库会话中，表示将要对数据库进行操作。
        # db.session.commit(): 提交数据库会话，将所有的操作（添加Book对象）应用到数据库中，实现数据的插入。
