from django.urls import	path
from.import	views
from django.conf.urls import url
from student.views import *


urlpatterns	=[		
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact-us/',views.contact_us,name="contact_us"),
    path('teacherdash/',views.teacher_dash,name='teacher_dash'), 
    path('teacher-profile/',views.teacher_profile,name="teacher_profile"),
    path('add_student_excel/',views.add_student_excel,name='add_student_excel'),
    path('mine/',views.ManageStudentListView.as_view(),name='manage_student_list'),
    path('<pk>/student/',views.student_list_view,name='student_list'),
    path('create/',views.StudentCreateView.as_view(),name='student_create'),				
    path('<pk>/edit/',views.StudentUpdateView.as_view(),name='student_edit'),				
    path('<pk>/delete/',views.StudentDeleteView.as_view(),name='student_delete'),
    path('<pk>/stuadmission/',views.student_admission,name='student_admission'),
    path('<pk>/studentfamily/',views.student_family_update,name='student_family_update'),
    path('<pk>/studentlg/',views.student_lg_update,name='student_lg_update'),
    path('<pk>/student-lg-edit/',views.student_lg_edit,name="student_lg_edit"),
    path('<pk>/studenthostel/',views.student_hostel_update,name='student_hostel_update'),
    path('<pk>/student-hostel-edit/',views.student_hostel_edit,name="student_hostel_edit"),
    path('<pk>/studentmedical/',views.student_medical_update,name='student_medical_update'),
    path('<pk>/studentbank/',views.student_bank_update,name='student_bank_update'),
    path('<pk>/studentplacement/',views.student_placement_update,name='student_placement_update'),
    path('<pk>/tgcalling/',views.tgcalling,name="tgcalling"),
    path('<pk>/teacher_student_dash/',views.teacher_student_dash,name='teacher_student_dash'),
    path('<pk>/studentaddress/',views.student_address_update,name='student_address_update'),
    path('<pk>/student-address-edit/',views.student_address_edit,name='student_address_edit'),
    path('<pk>/studentresident/',views.student_resident_update,name='student_resident_update'),
    path('<pk>/student-resident-edit/',views.student_resident_edit,name='student_resident_edit'),
    path('<pk>/studentfee/',views.student_fee_update,name='student_fee_update'),
    path('<pk>/<receipt>/student-fee-edit/',views.student_fee_edit,name='student_fee_edit'),
    path('<pk>/studentmidsem/',views.student_midsem_update,name='student_midsem_update'),
    path('<pk>/<sem>/<midterm>/student-midsem-edit/',views.student_midsem_edit,name="student_midsem_edit"),
    path('<pk>/studentresult/',views.student_result_update,name='student_result_update'),
    path('<pk>/<sem>/student-result-edit/',views.student_result_edit,name="student_result_edit"),
    path('<pk>/select_student/',views.t_attendance,name='select_student'),
    path('student_attendance/',views.studentattendance,name="student_attendance"),
    path('<pk>/attendance_view/',views.attendance_view,name='attendance_view'),
    path('<pk>/attendance_details/',views.attendance_details,name='attendance_details'),
    path('<pk>/<date>/attendance_update/',views.attendance_update,name='attendance_update'),
    path('<pk>/student_attendance_view',views.student_attendance_view,name="student_attendance_view"),
    path('<pk>/teacher_student_education',views.teacher_student_education,name="teacher_student_education"),
    path('<pk>/teacher_student_list/',views.teacher_student_list,name="teacher_student_list"),
    
    path('student_account_activate/',views.student_account_activate,name="student_account_activate"),
    path('teacher_subject/',views.teacher_subject,name="teacher_subject"),
    path('<subject_code>/<sem>/<sec>/subject_attendance/',views.subject_attendance,name="subject_attendance"),
    path('<subject_code>/<sem>/<sec>/subject_attendance_view/',views.subject_attendance_view,name="subject_attendance_view"),
    path('<pk>/subject_attendance_details/',views.subject_attendance_details,name="subject_attendance_details"),

    path('<pk>/<subject_code>/<date>/subject_attendance_update/',views.subject_attendance_update,name='subject_attendance_update'),
    path('<subject_code>/<sem>/<sec>/teacher_subject_mark/',views.teacher_subject_mark,name='teacher_subject_mark'),
    path('<subject_code>/<sem>/<sec>/teacher_subject_midterm/',views.teacher_subject_midterm,name='teacher_subject_midterm'),
    path('<subject_code>/<sem>/<sec>/teacher_practical_mark/',views.teacher_practical_mark,name='teacher_practical_mark'),
    path('<subject_code>/<sem>/<sec>/teacher_subject_midterm_view/',views.teacher_subject_midterm_view,name='teacher_subject_midterm_view'),
    path('<pk>/<subject_code>/<exam_no>/teacher_subject_midterm_update/',views.teacher_subject_midterm_update,name="teacher_subject_midterm_update"),
    path('<subject_code>/<sem>/<sec>/teacher_practical_mark_view/',views.teacher_practical_mark_view,name='teacher_practical_mark_view'),
    path('<pk>/<subject_code>/teacher_student_practical_mark_view/',views.teacher_student_practical_mark_view,name='teacher_student_practical_mark_view'),
    path('<pk>/<subject_code>/<practical_no>/teacher_student_practical_mark_update/',views.teacher_student_practical_mark_update,name='teacher_student_practical_mark_update'),
    path('<subject_code>/<sem>/<sec>/teacher_unit_mark_view/',views.teacher_unit_mark_view,name='teacher_unit_mark_view'),
    path('<pk>/<subject_code>/teacher_student_unit_mark_view/',views.teacher_student_unit_mark_view,name='teacher_student_unit_mark_view'),
    path('<pk>/<subject_code>/<exam_type>/<exam_no>/<unit_no>/teacher_student_unit_mark_update/',views.teacher_student_unit_mark_update,name='teacher_student_unit_mark_update'),
    path('<subject_code>/<sem>/<sec>/teacher_project_mark/',views.teacher_project_mark,name='teacher_project_mark'),
    path('<subject_code>/<sem>/<sec>/teacher_project_mark_view/',views.teacher_project_mark_view,name='teacher_project_mark_view'),
    path('<pk>/<subject_code>/teacher_project_mark_update/',views.teacher_project_mark_update,name='teacher_project_mark_update'),
    path('tg-student-attendance/',views.tg_student_attendance,name="tg_student_attendance"),
    path('tg-student-attendance-week/',views.tg_student_attendance_week,name="tg_student_attendance_week"),
    path('tg-student-attendance-date/',views.tg_student_attendance_date,name="tg_student_attendance_date"),
    path('<pk>/<message_type>/<attendance>/attendance-nofification/',views.attendance_notification,name="attendance_notification"),
    path('<pk>/student-attendance/',views.teacher_student_sem_attendance,name='teacher_student_sem_attendance'),
    path('<pk>/subject-attendance/',views.teacher_student_subject_attendance,name='teacher_student_subject_attendance'),
    path('<pk>/student_subject/',views.teacher_student_subject,name="teacher_student_subject"),
    path('<pk>/<year>/<sem>/<subject_code>/student_unit_mark/',views.teacher_student_unit_mark,name="teacher_student_unit_mark"),
    path('<pk>/<year>/<sem>/<subject_code>/student_midterm_mark/',views.teacher_student_midterm_mark,name="teacher_student_midterm_mark"),
    path('<pk>/<year>/<sem>/<subject_code>/student_practical_mark/',views.teacher_student_practical_mark,name="teacher_student_practical_mark"),
    path('<pk>/<year>/<sem>/<subject_code>/student_project_mark/',views.teacher_student_project_mark,name="teacher_student_project_mark"),


 ]