import os

print("Antibody.py")
print("by Spencer Baumann")
print()
print("Antivirus you can trust.")

def wouldyouliketoremove(pathtovirus):
    yorn = input("Would you like to remove it? (y/n): ")
    while yorn != "y" and yorn != "n":
        yorn = input("Would you like to remove it? (y/n): ")
    else:
        if yorn == "y":
            print("Removing the crappy virus...")
            os.remove(pathtovirus)
            print("Crappy virus obliterated! :D")
        elif yorn == "n":
            print("Okay, be careful out there.")

scan = input("Would you like to scan? (y/n): ").lower()
if scan == "y":
    print("Scanning. Please wait.")
    root = "C:\\"
    for (paths, dirs, files) in os.walk(root):
        for file in files:
            if file.endswith("olcamsrv.dll") or file.endswith("80000000.@"):
                print("Found Trojan: Win64/Sirefef.W!")
                print("Sirefef.W is a harmful trojan horse that can run adware, data-mining operations, CPU harnessing, and much more.")
                wouldyouliketoremove(os.path.join(paths, file))
    print("Done!")
