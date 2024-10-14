def find_and_click(wait, ec, by, value):
    """Finds and clicks an element by provided method and its value"""
    try:
        element = wait.until(ec.element_to_be_clickable((by, value)))
        element.click()
    except Exception as e:
        print(f"Error clicking element {value}: {e}")


def input_data(wait, ec, by, value, data, *args):
    """Finds and inputs data to an element by provided method and its value;
    possible to provide args which are keys that will be pressed after inputting data"""
    try:
        element = wait.until(ec.element_to_be_clickable((by, value)))
        if args:
            element.send_keys(data, *args)
        else:
            element.send_keys(data)
    except Exception as e:
        print(f"Error clicking element {value}: {e}")
