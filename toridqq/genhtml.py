import os
import string


class GenerateHtml:
    def __init__(self):
        self.dir_of_list = os.listdir("./images")
        self.img_html = None
        self.html_string = None

    def get_img_html(self):
        img_html = ""
        for dr in self.dir_of_list:
            if dr != "model":
                new_img_label = f"<h2>{dr}</h2><img src='./images/{dr}/new_pic.png' alt=''>"
                # old_img_label = f"<img src='./images/{dr}/old_pic.png' alt=''>"
                img_html = img_html + new_img_label
        return img_html

    def get_html(self):
        with open("./toridqq/html/template_html.html", 'r', encoding="utf-8") as fp1:
            template_html = fp1.read()

        data_dict = {"img_html": self.img_html}
        template = string.Template(template_html)
        self.html_string = template.substitute(data_dict)
        return self.html_string

    def gen_html_file(self):
        self.img_html = self.get_img_html()
        if self.img_html:
            with open("./show_img.html", "w", encoding="utf-8") as fp2:
                fp2.write(self.get_html())
