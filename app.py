from flask import Flask, render_template
import random

app = Flask(__name__)

def create_pairs(people):
    random.shuffle(people)
    pairs = []
    for i in range(0, len(people), 2):
        if i+1 < len(people):
            pairs.append((people[i], people[i+1]))
        else:
            # In case of odd number of people, one person will be left out
            pairs.append((people[i], None))
    return pairs

@app.route('/')
def generate_pairs():
    people = ['آ.منى أبو البرغل', 'تسنيم', 'آلاء', 'نور', 'أميرة', 'مروة', 'ريم', 'ريما', 'سجى', 'ندى',
          'آية', 'هبة', 'غزل', 'دعاء', 'رؤى', 'إيناس', 'دانية', 'سماح']
    pairs = create_pairs(people)
    return render_template('index.html', pairs=pairs)

if __name__ == '__main__':
    app.run(debug=True)
