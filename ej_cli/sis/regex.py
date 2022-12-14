matches = {
    "student_name": r"\s*\"ctl00_lblUser\" title=\s*\".*\"><span style='font-size:9px'>(.*?)(?=</)",
    "student_id": r"\s*\"ctl00_lblUser\" title=\s*\"(.*?)(?=\">)",
    "faculty": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_lblFaculty\">(.*?)(?=</)",
    "admission_year": r"\s*\"ctl00_lblAdmYear\">(.*?)(?=</)",
    "current_semester": r"\s*\"ctl00_lblAdmSem\">(.*?)(?=</)",
    "gender": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_StudentDtlPopup_ucStudDtlsTabsGnrlCtrl_TabHeader1_Tab_UcStudentBasicDataTabs_0_ucTabHeader_Tab_StudBasicData_View_0_lblGender\">(.*?)(?=</)",
    "nationality": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_StudentDtlPopup_ucStudDtlsTabsGnrlCtrl_TabHeader1_Tab_UcStudentBasicDataTabs_0_ucTabHeader_Tab_StudBasicData_View_0_lblFirstNationality\">(.*?)(?=</)",
    "national_id": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_StudentDtlPopup_ucStudDtlsTabsGnrlCtrl_TabHeader1_Tab_UcStudentBasicDataTabs_0_ucTabHeader_Tab_StudBasicData_View_0_txtNationalNum\" MaxLength=\s*\".*\">(.*?)(?=</)",
    "birth_date": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_StudentDtlPopup_ucStudDtlsTabsGnrlCtrl_TabHeader1_Tab_UcStudentBasicDataTabs_0_ucTabHeader_Tab_StudBasicData_View_0_txtBirthDate\">(.*?)(?=</)",
    "email": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_StudentDtlPopup_ucStudDtlsTabsGnrlCtrl_TabHeader1_Tab_UcStudentBasicDataTabs_0_ucTabHeader_Tab_StudBasicData_View_0_txtEmail\">(.*?)(?=</)",
    "mobile": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_StudentDtlPopup_ucStudDtlsTabsGnrlCtrl_TabHeader1_Tab_UcStudentBasicDataTabs_0_ucTabHeader_Tab_StudBasicData_View_0_txtMobileNo\">(.*?)(?=</)",
    "degree": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_lblScDegree\">(.*?)(?=</)",
    "student_major": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_lblMajior\">(.*?)(?=</)",
    "level": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_LblLvl\">(.*?)(?=</)",
    "enrollment_status": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_lblEnrollStatus\">(.*?)(?=</)",
    "academic_status": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_lblAcadmicStatus\">(.*?)(?=</)",
    "passed_ch": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_lblTotPassedCh\"\s*>\s*<\s*b\s*>\s*<\s*font\s*color\s*=\s*\"Black\"\s*>(.*?)(?=</)",
    "cgpa": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_lbLCGPA\"\s*>\s*<\s*b\s*>\s*<\s*font\s*color\s*=\s*\"Black\"\s*>(.*?)(?=</)",
    "notifications": r"\s*\<LI>\s*\<.*?>(.*?)(?=</)",
    "courses_codes": r"\s*\"ctl00_cntphmaster_grdAttendanceFW_ct.*_txtCourseCode\"\s.*>(.*?)(?=</)",
    "courses_names": r"\s*\"ctl00_cntphmaster_grdAttendanceFW_ct.*_Label2\">(.*?)(?=</)",
    "absence_times": r"\s*\"ctl00_cntphmaster_grdAttendanceFW_ct.*_Label3\">(.*?)(?=</)",
    "warnings": r"\s*\"ctl00_cntphmaster_grdAttendanceFW_ct.*_Label4\">(.*?)(?=</)",
    "advisor_name": r"\s*\"ctl00_cntphmaster_StudDataGeneralControl1_StudentDtlPopup_ucStudDtlsTabsGnrlCtrl_TabHeader1_Tab_UcStudentAcademicDataTabs_1_ucTabHeader_Tab_StudAcadData_View_0_LblAcadAdvisorName\">(.*?)(?=<\/)",
    "cal_week_days": r'\<td style="font-weight:bold;">(.*?)(?=\s*\<\/tr>)',
    "cal_courses_codes": r"Group: (.*?)(?= <)",
    "cal_courses_names": r"Course: (.*?)(?= <)",
    "cal_courses_types": r"Course Teaching: (.*?)(?= <)",
    "cal_times": r"<br \/>(.*?)(?=<)",
    "cal_buildings": r"Building: (.*?)(?= <)",
    "cal_rooms": r"Room: (.*?)(?= <)",
    "cal_instructors": r"Assistant: (.*?)(?= <)",
    "cal_day": r"^(.*?)(?=<\/td>)",
}
