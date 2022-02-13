import sys
import user.authentication
import transactions.journal
import banking.fvb.reconciliation

# print("Hello",sys.argv[1])
# print("Brave",sys.argv[1])
# print("new",sys.argv[1])
# print("World!",sys.argv[1])
# help("modules")

if __name__ == "__main__":
    #help("modules")
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        argv_list = "\n".join(sys.argv)
        print(argv_list)

    user.authentication.authenticate_user()
    transactions.journal.receive_income(100)
    transactions.journal.pay_expense(100)
    banking.fvb.reconciliation.do_reconciliation()

