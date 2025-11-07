import streamlit as st

# --- Budget Class ---
class budget:
    def __init__(self, budget_set, salary):
        self.set_budget = budget_set
        self.salary = salary

    def bud_show(self):
        st.write(f"**Salary:** {self.salary}  |  **Set Budget:** {self.set_budget}")

# --- Expense Class ---
class expence(budget):
    def __init__(self, salary, budget_set, expen={}):
        super().__init__(budget_set, salary)
        self.expen = expen
        self.exp_value = expen.values()

    def show(self):
        if self.set_budget < self.salary:
            if self.salary > sum(self.exp_value):
                st.subheader("📊 Expense Summary")
                st.write(f"**Total Expense:** {sum(self.exp_value)}")
                st.write(f"**Balance (Savings):** {self.salary - sum(self.exp_value)}")
                st.write(f"**Surplus Budget:** {self.set_budget - sum(self.exp_value)}")
                st.markdown("### 📈 Categorized by Percentage:")
                total = sum(self.exp_value)
                for k, v in self.expen.items():
                    st.write(f"- {k}: {v/total*100:.1f}%")
            else:
                st.error("❌ Expense is more than income!")
        else:
            st.error("❌ Budget is more than income!")

# --- Streamlit App UI ---
st.title("💸 Budget & Expense Analyzer")

salary = st.number_input("Enter your Salary", min_value=0, step=100)
budget_set = st.number_input("Enter your Budget", min_value=0, step=100)

expense_input = st.text_area("Enter Expenses as a dictionary (e.g. {'Food': 500, 'Rent': 1000})")

if st.button("Calculate"):
    try:
        # Use eval safely for dictionary parsing
        exp_dict = eval(expense_input, {"__builtins__": None}, {})

        if isinstance(exp_dict, dict) and all(isinstance(v, (int, float)) for v in exp_dict.values()):
            b = expence(salary, budget_set, exp_dict)
            st.divider()
            st.subheader("🔍 Budget Overview")
            b.bud_show()
            b.show()
        else:
            st.error("❌ Invalid dictionary format. Please use numeric values only.")
    except Exception as e:
        st.error("❌ Error in input. Make sure you enter a proper dictionary.")