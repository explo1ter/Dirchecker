import requests
import pyfiglet
import threading

print("\n" + "*" * 65)
print(pyfiglet.figlet_format("    DIRCHECKER"))
print("*\t\t\tBy Nibil Mathew\t\t\t\t*")
print("*\t\t\tgithub:explo1ter\t\t\t*")
print("\n" + "*" * 65)


fail = True


def check_dir(url, directory):
    dir_url = f"{url}/{directory}"
    response = requests.get(dir_url)
    if response.status_code == 200:
        print(f"Directory found : {directory}")
        global fail
        fail = False
    else:
        pass


def check_dir_main(url, wordlist, num_threads):
    try:
        with open(wordlist, 'r') as file:
            list = file.read().splitlines()
        threads = []
        for directory in list:
            if len(threads) >= num_threads:
                threads[0].join()
                threads.pop(0)
            thread = threading.Thread(target=check_dir, args=(url, directory))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    except Exception as e:
        print(f"Something went wrong {e}")


if __name__ == "__main__":
    url = input("Enter the absolute url of website : ")
    wordlist = input("Enter the path of wordlist : ")
    num_threads = int(input("Enter the number of threads(max=15) : "))
    if num_threads > 15:
        print("\nExceeded the thread limit\nExiting")
        exit(0)
    check_dir_main(url, wordlist, num_threads)
    if fail:
        print("\nCouldn't find a directory. Use another wordlist")
