from riddle import *

if not os.getenv("PORT"):
    os.environ["PORT"] = "8080"
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT')))

