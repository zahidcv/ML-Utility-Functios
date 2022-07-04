def cm_to_inch(value):
    return value/2.54
plt.figure(figsize=(cm_to_inch(10),cm_to_inch(6)))
plt.plot(history.history['loss'], color='b', label="Training loss")
plt.plot(history.history['val_loss'], color='r', label="validation loss")
legend = plt.legend(loc='best', shadow=True)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.savefig('validation color cnn', dpi = 300)
