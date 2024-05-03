from flask import Flask, render_template
import vk_api

app = Flask(__name__)

@app.route('/', methods=['GET'])
def VK():
    group_dict = [
        -186182760, #Ярославская область
        -172765605, # Администрация Переславля-Залесского
        -160270735, #Администрация города Рыбинска
        -168175327, #ГБУЗ ЯО Областная детская клиническая больница
        -56632874, #Мэрия города Ярославля
        -9571212, #Рыбинский Драматический Театр
        -147097661, #ГП Ярославской области " Северный водоканал"
        -173014865, #Департамент образования город Рыбинск  
        -171595855, #Ростовский район
        -170172175, #ГБУЗ ЯО "Областная клиническая больница"
    ]
    posts_data = []
    vk = vk_api.VkApi(token="dac09b2cdac09b2cdac09b2cc1d9d7debeddac0dac09b2cbf0c4dc7f5b6c8425556fc77")
    
    for group_id in group_dict:
        # Получаем только 2 новых поста из каждой группы
        posts = vk.method('wall.get', {'owner_id': group_id, 'count': 2})['items']
        for post in posts:
            post_data = {
                'widget_id': f'vk_post_{group_id}_{post["id"]}',
                'owner_id': post['owner_id'],
                'post_id': post['id'],
                'hash': post['hash'],
                'api_version': '5.0'  # Версия API для виджетов
            }
            posts_data.append(post_data)

    return render_template('index.html', posts=posts_data)

if __name__ == '__main__':
    app.run(debug=True)
