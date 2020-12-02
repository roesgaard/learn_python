import test_functions as tf


def main():
    """
    Run main port of script
    """
    response = tf.return_request()
    ip = tf.return_ip(response)
    print(f'Your IP is {ip}')


if __name__ == '__main__':
    # This part is run when first
    main()
