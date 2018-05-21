from riddle import *

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT')))

