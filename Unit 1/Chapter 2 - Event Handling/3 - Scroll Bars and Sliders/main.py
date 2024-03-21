# Scrollbars are useful while looking at large documents or images that cannot appear in a limited visible area.
# Scrollbars appear horizontally or vertically.
# Sliders are a way of selecting an integer value between two values.

#* A QScrollBar has the following controls:
#* Slider handle: This control is used to move to any part of the document or image quickly.
#* Scroll arrows: These are the arrows on either side of the scrollbars.
#* Page control: The page control is the background of the scrollbar over which the
# slider handle is dragged. The amount the slider handle moves can be
# specified via the pageStep property. The page step is the amount by which a
# slider moves when the user presses the Page Up and Page Down keys. You can set
# the amount of the pageStep property by using the setPageStep() method.

#* QScrollBar methods:
# value(): Gets the current value of the scrollbar
# setValue(): This method assigns value to the scrollbar
# minimum(): This method returns the minimum value of the scrollbar
# maximum(): This method returns the maximum value of the scrollbar
# setMinimum(): This method assigns the minimum value to the scrollbar
# setMaximum(): This method assigns the maximum value to the scrollbar
# setSingleStep(): This method sets the single step value
# setPageStep(): This method sets the page step value

#* QScrollBar provides only integer values.

#* QScrollBar signals:
# valueChanged(): This signal is emitted when the scrollbar's value is changed (moved)
# sliderPressed(): This signal is emitted when the user starts to drag the slider handle
# sliderMoved(): This signal is emitted when the user drags the slider handle
# sliderReleased(): This signal is emitted when the user releases the slider handle
# actionTriggered(): This signal is emitted when the scrollbar is changed by user interaction

# p72