# Wiegand_gen  
### ** The intent on this progam is to be used with testing security systems and create events in the history **  
> This program is written to work with a Raspberry Pi Pico.  This could work on any Iot device that allows use of MicroPython on the device.  You will have to manually add the created text file using the Wygen application.  The device will then read the text file and use the card numbers you created and send them to the system.  You can change what pins are used.  You have to edit the code.  

## Program device  
### Using Raspberry Pi Pico  
> You will have to save the text file to the pico also, be mindfull of the size of you text file for cards.  Also, if you have not setup you Pi Pico yet, I would suggest you follow this link: [Configure Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/0).  You do not have to continue once you have the firmware loaded.  
>
> 1. Load(save) script "main.py" onto Pi Pico.
> 2. save cards.txt created file to Pico, from where you executed the code generator.
> 3. Attach Pin 14 to D0 on controller.
> 4. Attach Pin 15 to D1 on controller.
> 5. Power on device, View event log. 
>> **You should notice card reads in your event log, possibly invalid.  Verify the card numbers and data connections to D0/D1.**
>> **Also, if you are not receiving any reads, your system may not except low voltage reads.  Meaning, it will not accept anything lower than 5 VDC.**
>> **This is due too the low operating voltage of the Pico.  It tops out at around 3.7 VDC.  So the peak drop is a 3 VDC difference in the signal that**
>> **sent to the controller.** 
