from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# 知识库数据，每个领域对应一个简单的描述
knowledge_data = {
    'science': '科学是系统地研究自然世界的结构和行为的学科。',
    'technology': '技术是应用科学知识以解决实际问题的方法和过程。',
    'mathematics': '数学是研究数量、结构、空间和变化等概念的学科。',
    'history': '历史是对过去事件的记录和分析，特别是人类社会的活动。',
}

@app.route('/')
def index():
    return render_template('index.html', knowledge_data=knowledge_data)

@app.route('/<domain>')
def knowledge(domain):
    if domain in knowledge_data:
        return render_template('knowledge.html', domain=domain, description=knowledge_data[domain])
    else:
        return "<h1>未找到该领域的知识</h1>"

if __name__ == '__main__':
    app.run(debug=True)


