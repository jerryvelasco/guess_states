import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")


image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

"""will get the coordinates of clicks we make on screen""" 
# #takes 2 values as input and prints them out
# def get_mouse_click_coordinates(x,y):
#  ı   print(x,y)

# #event listener, listens for when the mouse clicks and then its going to call method
# turtle.onscreenclick(get_mouse_click_coordinates)


#pop up box that will get the users guess 


data = pandas.read_csv("50_states.csv")

states = data.state.to_list()
correct_guesses = []

answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?:").title()
score = 0

continue_game = True

while continue_game:

    #loops through states list and checks if the answer is present
    if answer_state in states:
        correct_guesses.append(answer_state)
        screen_text = turtle.Turtle()
        screen_text.hideturtle()
        screen_text.penup()

        #selects the row using the state 
        state_info = data[data.state == answer_state]

        #using the states row info we grab the x and y coordinates and turn them into ints
        screen_text.goto(int(state_info.x), int(state_info.y))

        #then writes the state to the screen 
        screen_text.write(answer_state)

        score += 1

        

    elif len(correct_guesses) > 50:
        continue_game = False

     
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?:").title()

    #if the cancel button is pressed it stops the loop 
    if answer_state == None or answer_state == "Exit":
        missing_states = []
        for state in states: 
            if state not in correct_guesses:
                missing_states.append(state)

        new_df = pandas.DataFrame(missing_states)
        new_df.to_csv("missing_states.csv")
        continue_game = False
    
        
       







#keeps the screen open 
# turtle.mainloop()


