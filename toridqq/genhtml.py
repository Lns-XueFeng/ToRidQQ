import os


class GenerateHtml:
    def __init__(self):
        self.dir_of_list = os.listdir("./images")
        self.img_html = None
        self.style = "<style>html body{margin: 0 auto;text-align:center;color:pink;background:lightyellow;}" \
                     "img {border:purple 4px solid;}</style>"

    def get_img_html(self):
        img_html = ""
        for dr in self.dir_of_list:
            if dr != "model":
                new_img_label = f"<h2>{dr}</h2><img src='./images/{dr}/new_pic.png' alt=''>"
                old_img_label = f"<img src='./images/{dr}/old_pic.png' alt=''>"
                img_html = img_html + new_img_label + old_img_label
        return img_html

    def get_html(self):
        return f"<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'>" \
               f"<title>消息通知</title>{self.style}</head><body><h1>查看消息</h1><div>{self.img_html}</div></body></html>"

    def gen_html_file(self):
        self.img_html = self.get_img_html()
        if self.img_html:
            with open("./show_img.html", "w", encoding="utf-8") as fp:
                fp.write(self.get_html())
