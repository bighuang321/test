class Rectangle():
    lenth = 5.00
    width = 4.00

    def getRect(self):
        print('这个矩形的长是：%.2f, 宽是：%.2f' % (self.lenth, self.width))
    def setRect(self):
        print('请输入矩形的长和宽...')
        self.lenth = float(input('长：'))
        self.width = float(input('宽：'))
    def getArea(self):
        print(self.lenth * self.width)
