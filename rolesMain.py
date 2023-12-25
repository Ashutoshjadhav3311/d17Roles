import streamlit as st

def circular_shift(employees):
    num_employees = len(employees)

    current_roles = [employee['job_role'] for employee in employees]
    new_roles = [current_roles[-1]] + current_roles[:-1]
    for i in range(num_employees):
        employees[i]['job_role'] = new_roles[i]
    return employees

# Example Usage
if __name__ == "__main__":
    # List of employees with their current job roles
    employees_list = [
        {"name": "Ashutosh", "job_role": "kitchen"},
        {"name": "Nitin", "job_role": "Hall"},
        {"name": "Devansh", "job_role": "Hallway stairs"},
        {"name": "Tejas", "job_role": "Mop"},
        {"name": "Arpit", "job_role": "Tiolet"}
    ]

    # Streamlit app title
    st.title('D17 Job Roles ')

    # Display the initial job roles
    st.write("Select Roles you had Last week from the menu")
    

    # Take job role inputs for all users from the user
    #st.write("\nUpdate Job Roles:")
    for employee in employees_list:
        new_job_role = st.selectbox(f"Select the new job role for {employee['name']}", ["Kitchen", "Hall", "Hallway stairs", "Mop", "Tiolet"], index=0)
        employee['job_role'] = new_job_role

    # Button to trigger circular shift
    if st.button("Run"):
        # Perform circular shift
        updated_roles = circular_shift(employees_list)

        # Display the updated job roles after the circular shift
        st.write("\nUpdated Job Roles:")
        for employee in updated_roles:
            st.write(f"{employee['name']}: {employee['job_role']}")
