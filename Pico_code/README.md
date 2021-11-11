# Wiegand_gen  
### ** The intent on this progam is to be used with testing security systems and create events in the history **  
> This program is written to work with a Raspberry Pi Pico.  This could work on any Iot device that allows use of MicroPython on the device.  You will have to manually add the created text file using the Wygen application.  The device will then read the text file and use the card numbers you created and send them to the system.  You can change what pins are used.  You have to edit the code.  

## Program device  
### Using Raspberry Pi Pico  
> You will have to save the text file to the pico also, be mindfull of the size of you text file for cards.  Also, if you have not setup you Pi Pico yet, I would suggest you follow this link: [Configure Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/0).  You do not have to continue once you have the firmware loaded.  
>
> 1. Load program onto Pi Pico.
> 2. Add card.txt created file to Pico.
> 3. Attach Pin 14 to D0 on controller.
> 4. Attach Pin 15 to D1 on controller.
> 5. Power on device, View event log.
