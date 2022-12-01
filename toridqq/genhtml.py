import os


class GenerateHtml:
    def __init__(self):
        self.dir_of_list = os.listdir("./images")
        self.img_html = ""

    def get_img_html(self):
        img_html = ""
        for dir in self.dir_of_list:
            if dir != "model":
                new_img_label = f"<h2>{dir}</h2><img src='./images/{dir}/new_pic.png' alt=''>"
                old_img_label = f"<img src='./images/{dir}/old_pic.png' alt=''>"
                img_html = img_html + new_img_label + old_img_label
        return img_html

    def get_html(self):
        return f"<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'>" \
               f"<title>消息通知</title></head><body><h1>查看消息</h1><div>{self.img_html}</div></body></html>"

    def gen_html_file(self):
        self.img_html = self.get_img_html()
        if self.img_html:
            with open("./show_img.html", "w", encoding="utf-8") as fp:
                fp.write(self.get_html())
