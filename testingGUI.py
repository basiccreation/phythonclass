import tkinter
import tkinter.messagebox

class GUI:
    
    def __init__(self):

        # Set up window / Creates root widget
        self.main_window = tkinter.Tk()
        
        # Create Frames
        self.intro_frame = tkinter.Frame(self.main_window)
        self.data_input_frame = tkinter.Frame(self.main_window)
        self.data_output_button_frame = tkinter.Frame(self.main_window)
        self.data_output_frame = tkinter.Frame(self.main_window)
        self.radio_frame = tkinter.Frame(self.main_window)

        # Pack Frames
        self.intro_frame.pack()
        self.data_input_frame.pack()
        self.data_output_frame.pack()
        self.data_output_button_frame.pack()
        self.radio_frame.pack()

        #------------------------------------------------
        # Create a quit button
        self.close_button = tkinter.Button(self.intro_frame,
                                 text = "Close window", width = 10,
                                 command = self.main_window.destroy)
        
         # Pack quit button
        self.close_button.pack(side = "top")

        # Creates label widget and assigns to self.main_window
        self.intro_label = tkinter.Label(self.intro_frame,
                               width = 40,
                               text="\nEnter distance in km or miles"+\
                                         "\nand convert\n")
        
        # Pack label widget
        self.intro_label.pack(side="left")
        #------------------------------------------------
        # Prompt user to enter distance
        self.prompt_label = tkinter.Label(self.data_input_frame,
        text ="Enter the distance:")

        # Pack prompt label
        self.prompt_label.pack(side = "left")

        # Add Field to enter number
        self.distance_entry = tkinter.Entry(self.data_input_frame,
                                            width = 10)
        # Pack distance_entry field
        self.distance_entry.pack(side = "right")

        #------------------------------------------------
        # Create a calculate miles button
        self.calc_mls_button = tkinter.Button(self.data_output_button_frame,
                                 text = ".. miles",
                                 command = self.convert_to_miles)
        # Create a calculate kilometers button
        self.calc_km_button = tkinter.Button(self.data_output_button_frame,
                                 text = "... kilometers",
                                 command = self.convert_to_km)
        # Pack miles button
        self.calc_mls_button.pack(side = "left")
        
        # Pack kilometers button
        self.calc_km_button.pack(side = "right")
        
        #------------------------------------------------

        # The result of the calculation
        self.result_label = tkinter.Label(self.data_output_frame,
        text ="Converts to:")

        # Pack results label
        self.result_label.pack(side = "left")

        # StringVar object to associate the output label
        self.value = tkinter.StringVar()

        self.miles_label = tkinter.Label(self.data_output_frame, textvariable = self.value)

        # Pack the miles_label
        self.miles_label.pack(side = "right")

        
        
        #------------------------------------------------
        # Create the intVar to go with the radio button
        self.radio_var = tkinter.IntVar()

        # Set intVar to 1
        self.radio_var.set(1)

        #Create radio buttons
        self.rb1 = tkinter.Radiobutton(self.radio_frame,
                                       text = "Red Pill",
                                       variable = self.radio_var,
                                       value = 1,command = self.radio_method)
        self.rb2 = tkinter.Radiobutton(self.radio_frame,
                                       text = "Blue Pill",
                                       variable = self.radio_var,
                                       value = 2,command = self.radio_method)

        # Pack the radion buttons
        self.rb1.pack(side = "left")
        self.rb2.pack(side = "left")
        #------------------------------------------------
        # Execute tkinter module's mainloop function
        tkinter.mainloop()

    # Calculation functions
    def convert_to_miles(self):
        entry = float(self.distance_entry.get())
        miles = entry * 0.6214
        self.value.set(str(miles) + " miles")
        
    def convert_to_km(self):
        entry = float(self.distance_entry.get())
        km = entry * 1.6214
        self.value.set(str(km) + " km")

    def radio_method(self):
        choice = str(self.radio_var.get())
        self.value.set(choice)

gui = GUI()
