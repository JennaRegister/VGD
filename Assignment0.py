alice_account = 1.0
bob_account = 100000.0

printed_past = False

for year in range(2015):
    alice_interest = alice_account * 0.05
    alice_account = alice_account + alice_interest

    bob_interest = bob_account * 0.04
    bob_account = bob_account + bob_interest

    if alice_account > bob_account and not printed_past:
        print("Alice had more than Bob after the ", year, "th year", sep="")
        printed_past = True

print("Alice currently has $", alice_account, sep="")
print("Bob currently has $", bob_account, sep="")