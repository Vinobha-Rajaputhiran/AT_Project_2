"""
orange_data.py

Program : File containing the Data for OrangeHRM
"""

class OrangeHRM_Data:

    # Webpage URLs data
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url_login = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    dashboard_url_forgot_password = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"
    dashboard_url_admin_page = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"

    # User Data
    admin_username = "Admin"
    positive_password = "admin123"
    forgot_password_username = "Deadpool"

    # Validation Data
    password_reset_message = "Reset Password link sent successfully"
    title = "OrangeHRM"
    header_options = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Corporate Branding", "Configuration"]
    main_menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Claim", "Buzz"]


