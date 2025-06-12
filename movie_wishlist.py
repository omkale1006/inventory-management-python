# movie wishlist (python project)

# Step 1: Shuruat me kuch favourite movies
movie_list = ["Mahakal", "Baaghi", "Pushpa", "Pushpa 2"]

while True:
    print("\n🎥 Movie Wishlist App")
    print("1. Movie list dikhaye")
    print("2. Nayi movie add karein")
    print("3. Koi movie delete karein")
    print("4. Program band karein")

    choice = input("choose the  option (1-4): ")

    if choice == "1":
        print("📃 Aapki Movie List:", movie_list)

    elif choice == "2":
        new_movie = input("Kaunsi movie add karni hai? ")
        movie_list.append(new_movie)
        print(f"✅ '{new_movie}' movie add ho gayi!")

    elif choice == "3":
        del_movie = input("Kaunsi movie delete karni hai? ")
        if del_movie in movie_list:
            movie_list.remove(del_movie)
            print(f"❌ '{del_movie}' movie delete ho gayi.")
        else:
            print("⚠️ Movie list me nahi mili!")

    elif choice == "4":
        print("🙏 Dhanyavaad! Aapka Movie Wishlist band ho gaya.")
        break

    else:
        print("❌ Kripya sahi vikalp chuniye (1-4).")
