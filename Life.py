from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # 提供一个简单的HTML表单来接受用户输入
    return '''
    <form action="/analyze" method="post">
      <label for="age">Age:</label>
      <input type="number" id="age" name="age"><br><br>
      <label for="result">Self-reported mood level (1-10):</label>
      <input type="number" id="mood" name="mood" min="1" max="10"><br><br>
      <input type="submit" value="Submit">
    </form>
    '''


@app.route('/analyze', methods=['POST'])
def analyze():
    # 从请求中获取用户的输入数据
    try:
        age = int(request.form['age'])
        mood_level = int(request.form['mood'])
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input data'})

    # 简单的分析逻辑【注意：在实际应用中，应该使用更复杂和基于研究基础的模型】
    # 举例：假设 mood_level 低于 5，风险增加（这里只是示例）
    risk_score = 100 - (mood_level / 10 * 100)

    if risk_score > 50:
        risk_assessment = "High"
    else:
        risk_assessment = "Low"

    # 返回分析结果
    return jsonify({
        'age': age,
        'mood_level': mood_level,
        'risk_score': risk_score,
        'risk_assessment': risk_assessment
    })


if __name__ == '__main__':
    app.run(debug=True)