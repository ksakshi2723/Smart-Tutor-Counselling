from django.urls import	path
from.import	views
from django.conf.urls import url
from user.views import *

from django.contrib.auth	import	views   as	auth_views


urlpatterns	=[		
    path('hoddash/',views.hod_dash,name='hod_dash'),
    path('hod-profile/',views.hod_profile,name="hod_profile"),
    path('departmentfaculty/',views.department_faculty,name='department_faculty'),
    path('facultyaccountrequest/',views.faculty_account_request,name='faculty_account_request'),
    path('facultyaccountactivate/',views.faculty_account_activate,name='faculty_account_activate'),
    path('attendance_report/',views.attendance_report,name="attendance_report"),
    path('<year>/attendance_pdf/',views.generate_attendance_pdf,name="attendance_pdf"),
    path('<year>/download_attendance_pdf/',views.download_attendance_pdf,name="download_attendance_pdf"),
    path('add_subject/',views.add_subject,name="add_subject"),
    path('subject_view',views.subject_view,name="subject_view"),
    path('<sem>/<subject_code>/subject/',views.subject_update,name="subject_update"),
    path('<sem>/<subject_code>/subject_delete/',views.subject_delete,name="subject_delete"),
    path('<sem>/<subject_code>/subject_delete_confirm/',views.subject_delete_confirm,name="subject_delete_confirm"),
    path('syllabus/',views.syllabus,name="syllabus"),
    path('syllabus_view',views.syllabus_view,name="syllabus_view"),
    path('<sem>/syllabus_update/',views.syllabus_update,name="syllabus_update"),
    path('<sem>/syllabus_delete/',views.syllabus_delete,name="syllabus_delete"),
    path('<sem>/syllabus_delete_confirm/',views.syllabus_delete_confirm,name="syllabus_delete_confirm"),
    path('<year>/<sem>/syllabus/',views.sem_syllabus,name="sem_syllabus"),		
    path('assign_ct/',views.assign_ct,name="assign_ct"),
    path('<sem>/<sec>/add_assign_ct',views.add_assignct,name="add_assignct"),
    path('class_view/',views.class_view,name='class_view'),
    path('<subject_code>/<sem>/<sec>/class_teacher_update/',views.class_teacher_update,name="class_teacher_update"),
    path('<dept>/students/',views.department_student,name="department_student"),
    path('assign-tg/',views.assign_tg,name="assign_tg"),
    path('update-tg/',views.update_tg,name="update_tg"),
    path('tg_updated/',views.tg_updated,name="tg_updated"),
    path('<pk>/',views.hod_student_view,name="hod_student_view"),
    path('<pk>/tgcalls/',views.hod_student_tg_call,name="hod_student_tg_call"),
    path('<pk>/studentmidsem/',views.hod_student_midsem,name='hod_student_midsem'),
    path('<pk>/<sem>/<midterm>/student-midsem-edit/',views.hod_student_midsem_edit,name="hod_student_midsem_edit"),
    path('<pk>/studentresult/',views.hod_student_result,name='hod_student_result'),
    path('<pk>/<sem>/student-result-edit/',views.hod_student_result_edit,name="hod_student_result_edit"),
    path('<pk>/stuadmission/',views.hod_student_admission,name='hod_student_admission'),
    path('<pk>/studenthostel/',views.hod_student_hostel,name='hod_student_hostel'),
    path('<pk>/student-hostel-edit/',views.hod_student_hostel_edit,name="hod_student_hostel_edit"),
    path('<pk>/student-placement/',views.hod_student_placement,name='hod_student_placement'),
    path('<pk>/studentfee/',views.hod_student_fee_update,name='hod_student_fee_update'),
    path('<pk>/<receipt>/student-fee-edit/',views.hod_student_fee_edit,name='hod_student_fee_edit'),
    path('<pk>/hod-student-education',views.hod_student_education,name="hod_student_education"),
    path('<pk>/studentfamily/',views.hod_student_family,name='hod_student_family'),
    path('<pk>/studentlg/',views.hod_student_lg,name='hod_student_lg'),
    path('<pk>/student-lg-edit/',views.hod_student_lg_edit,name="hod_student_lg_edit"),
    path('<pk>/studentmedical/',views.hod_student_medical,name='hod_student_medical'),
    path('<pk>/studentbank/',views.hod_student_bank,name='hod_student_bank'),
    path('<pk>/student-attendance',views.hod_student_attendance,name="hod_student_attendance"),
    path('<pk>/<message_type>/<attendance>/attendance-nofification/',views.hod_attendance_notification,name="hod_attendance_notification"),
    path('<pk>/student-edit/',views.hod_student_edit,name="hod_student_edit"),
    path('<pk>/student-attendance/',views.hod_student_sem_attendance,name='hod_student_sem_attendance'),
    path('<pk>/subject-attendance/',views.hod_student_subject_attendance,name='hod_student_subject_attendance'),
    ]