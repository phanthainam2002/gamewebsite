from flask import Flask, render_template, redirect
import mlab
from mongoengine import *

app = Flask(__name__)

mlab.connect()
class Gamelist(Document):
    name = StringField()
    description = StringField()
    image = StringField()


#
# gl = gamelist(name="Dying Light",
#             description="Dying Light là một tựa game sinh tồn lấy đề tài zombie cực kỳ ấn tượng của Techland, cha đẻ series game thế giới mở Dead Island được nhiều game thủ Việt yêu mến. Nếu như Dead Island ít nhiều mang tính chất giải trí và không quá nghiêm trọng thì Dying Light lại khắc họa bối cảnh của một thời kì đầy đen tối khi loài người bị đe dọa bởi đại dịch zombie.",
#             image="https://i.ytimg.com/vi/V3RfeSKSk_g/maxresdefault.jpg")
# gl.save()

# data_fake = [
#
#
# {
# "name" : "Dying Light",
# "description" : " Dying Light là một tựa game sinh tồn lấy đề tài zombie cực kỳ ấn tượng của Techland, cha đẻ series game thế giới mở Dead Island được nhiều game thủ Việt yêu mến. Nếu như Dead Island ít nhiều mang tính chất giải trí và không quá nghiêm trọng thì Dying Light lại khắc họa bối cảnh của một thời kì đầy đen tối khi loài người bị đe dọa bởi đại dịch zombie.",
# "image" : "https://i.ytimg.com/vi/V3RfeSKSk_g/maxresdefault.jpg",
# },
# {
# "name" : "Assassins Creed Unity 2",
# "description" : "Assassin’s Creed: Unity là phiên bản tiếp theo trong series sát thủ đã quá nổi tiếng Assassin’s Creed, ngay từ khi chính thức xuất đầu lộ diện với danh nghĩa phiên bản thứ 5 của dòng game, những gì mà người hâm mộ được chứng kiến là sự choáng ngợp của đồ họa, hệ thống gameplay được cải tiến vượt bậc, hứa hẹn một siêu phẩm hay nhất từ trước đến nay.",
# "image" : "http://tructiepgame.com/wp-content/uploads/2016/11/Assassins-Creed-Unity-2.jpg",
# },
# {
# "name" : "ShaDow Warrior",
# "description" : "Shadow Warrior 2 là tựa game hành động kết hợp bắn súng và chặt chém, trò chơi là một sự cân bằng và kết hợp tuyệt vời giữa Path of Exile và Doom, mang đến cho bạn nhiều lối chơi và phong cách giải trí khác nhau, từ chiến đấu cổ điển với cung và kiếm cho đến vũ trang hiện đại với súng ống, lựu đạn.",
# "image" : "http://tructiepgame.com/wp-content/uploads/2016/12/Shadow-Warrior-2-2.jpg",
# },
# {
# "name" : "I'm Alive"'',
# "description" :  "I Am Alive là tựa game sinh tồn đi theo lối hành động giải đố, khá giống với dòng game Uncharted, cũng có nhưng pha lèo trèo và chiến đấu mạo hiểm, chỉ khác là rừng rậm nay đã được thay thế bằng những tòa nhà chọc trời và Adam không có nhiều thời gian cũng như sức lực bởi mỗi phút trôi qua, anh sẽ phải trả giá bằng lượng stamina ít ỏi của mình.",
# "image" : "http://tructiepgame.com/wp-content/uploads/2017/03/3-1.jpg",
# }
# ]
#
# for data in data_fake:
#     name = data["name"]
#     description = data["description"]
#     image = data['image']
#     gl =  Gamelist(name = name,description=description,image = image,
#     )
#     gl.save()





@app.route('/')
def index():
    return render_template('index.html', gamelist = Gamelist.objects)
@app.route('/admin')
def admin():
    return render_template("admin.html", gamelist = Gamelist.objects)
@app.route("/delete_game/<game_id>")
def deleting(game_id):
    game_list=Gamelist.objects().with_id(game_id)
    if game_list is not None:
        game_list.delete()
        return redirect ("/admin")
    return redirect ("/")

@app.route('/edit_game/<game_id>')
def edit(game_id):
    game_list=Gamelist.objects().with_id(game_id)
    if game_list is not None:
        return render_template ("game_info_edit.html")

@app.route('/game_info/<game_id>')
def gameinfo(game_id):
    game_list=Gamelist.objects().with_id(game_id)
    if game_list is not None:
         return render_template ("game_info.html",gamelist=game_list)
    return "not loading"



if __name__ == '__main__':
  app.run( debug=True)
