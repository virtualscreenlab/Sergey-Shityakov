def clear_main_log():
    main_log_file = open('log.txt', 'w')
    main_log_file.write('')
    main_log_file.close()


def merge_logs():
    clear_main_log()
    main_log_file = open('log.txt', 'a')
    for log_file in ['azides_log.txt', 'alkynes_log.txt', 'parameters_log.txt', 'products_log.txt', 'imgs_log.txt']:
        try:
            f = open(log_file)
            data = f.read()
            main_log_file.write(data)
            main_log_file.write('\n\n')
            f.close()
        except Exception:
            pass
    main_log_file.close()
