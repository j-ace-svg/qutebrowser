#!/bin/bash

# Open the inputed address
echo "open -t -r $@" >> "$QUTE_FIFO"

# Move the new tab up
echo "tab-move -" >> "$QUTE_FIFO"
