from vellum import VellumDocument
from vellum.workflows.inputs import DatasetRow
from vellum.workflows.sandbox import WorkflowSandboxRunner

from .inputs import Inputs
from .workflow import Workflow

dataset = [
    DatasetRow(
        label="IMPROVED Note - Complete Progress Note (Best Practice)",
        inputs=Inputs(
            clinical_dictation="""Progress Note - January 19, 2023

CHIEF COMPLAINT:
Medication refill, insurance change, and routine chronic disease management follow-up for multiple comorbidities.

HISTORY OF PRESENT ILLNESS:
66 year old male with multiple chronic conditions presents for routine follow-up, medication refills, and insurance transition.

**Type 2 Diabetes Mellitus:**
- Diagnosed 8 years ago, on oral agents
- Home glucose monitoring: fasting 130-160 mg/dL (above goal)
- Last A1c 3 months ago: 7.8% (above goal of <7%)
- Adherent to metformin and glipizide
- Denies hypoglycemic episodes, polyuria, polydipsia
- Denies vision changes, numbness/tingling in extremities
- Last diabetic eye exam: 8 months ago - no retinopathy noted
- Last podiatry visit: 6 months ago - no ulcers or neuropathy

**Hypertensive Heart Disease:**
- Diagnosed 10 years ago, on dual therapy
- Home BP readings: 130-145/80-88 mmHg (at goal)
- Adherent to amlodipine and losartan
- Denies chest pain, palpitations, dyspnea on exertion
- Denies orthopnea, PND, lower extremity edema
- Last echocardiogram 1 year ago: EF 55%, no LVH

**Chronic Gout:**
- History of recurrent gout flares, primarily right great toe
- Last acute flare: 4 months ago, resolved with colchicine
- Currently asymptomatic, no joint pain or swelling
- On maintenance therapy

**Mood Disorder (Unspecified):**
- Followed by psychiatry, stable on current regimen
- Denies depressed mood, anhedonia, sleep disturbance
- Denies suicidal or homicidal ideation
- Adherent to psychiatric medications

**Anemia:**
- Discovered 6 months ago, iron deficiency suspected
- On iron supplementation
- Denies fatigue, weakness, melena, hematochezia
- Denies heavy bleeding from any source

**Mixed Hyperlipidemia:**
- On statin therapy
- Last lipid panel 4 months ago: LDL 102, HDL 38, TG 180
- Tolerating atorvastatin without myalgias

**Proteinuria:**
- Incidental finding on routine UA
- On ACE-I/ARB for renal protection
- No known CKD diagnosis

**Atherosclerosis of Aorta:**
- Incidental finding on imaging
- Asymptomatic, no claudication

REVIEW OF SYSTEMS:
Constitutional: Denies fever, chills, night sweats, unintentional weight loss or gain, fatigue
HEENT: Denies headache, vision changes, hearing loss, sore throat
Cardiovascular: Denies chest pain, palpitations, orthopnea, PND, lower extremity edema, claudication
Respiratory: Denies dyspnea, cough, wheezing, hemoptysis
Gastrointestinal: Denies nausea, vomiting, abdominal pain, diarrhea, constipation, melena, hematochezia
Genitourinary: Denies dysuria, hematuria, frequency, urgency, nocturia (1x)
Musculoskeletal: Denies joint pain, swelling, stiffness, muscle weakness
Neurological: Denies numbness, tingling, weakness, dizziness, syncope
Psychiatric: Mood stable, denies depression, anxiety, SI/HI
Skin: Denies rashes, lesions, wounds
Endocrine: Denies heat/cold intolerance, polydipsia, polyuria

PHYSICAL EXAMINATION:
Vitals: BP 138/84 mmHg, HR 72 bpm regular, RR 16, Temp 98.2F, Weight 198 lbs (stable), Height 5\'9\", BMI 29.2, SpO2 98% RA
General: Alert, oriented x3, no acute distress, well-nourished, well-groomed
HEENT: Normocephalic, atraumatic. Pupils equal, round, reactive. Oropharynx clear, moist mucous membranes.
Neck: Supple, no lymphadenopathy, no thyromegaly, no JVD
Cardiovascular: Regular rate and rhythm, S1/S2 normal, no murmurs, rubs, or gallops. No peripheral edema. Pedal pulses 2+ bilaterally.
Respiratory: Clear to auscultation bilaterally, no wheezes, rhonchi, or crackles.
Abdomen: Soft, non-tender, non-distended. Normoactive bowel sounds. No hepatosplenomegaly.
Extremities: No cyanosis, clubbing, or edema. Warm and well-perfused. No joint swelling or erythema.
Neurological: CN II-XII intact. Strength 5/5 all extremities. Sensation intact. Monofilament test: intact bilateral feet (10/10).
Skin: No rashes, ulcers, or lesions. Feet examined: no calluses, no interdigital maceration, nails intact.
Psychiatric: Appropriate mood and affect, normal speech, coherent thought process.

RESULTS REVIEWED:
Labs (today): HbA1c 7.6% (improved from 7.8%), FBG 142, BMP: Na 140, K 4.2, Cr 1.1, eGFR 72
Lipid panel: TC 195, LDL 98, HDL 40, TG 158
CBC: WBC 6.8, Hgb 12.8 (improved from 11.2), Plt 245
Uric acid: 7.2, Urine microalbumin/creatinine ratio: 45 mg/g (mildly elevated)
Prior Echo (1 year ago): EF 55%, no LVH, no valvular abnormalities

ASSESSMENT & PLAN:

1. Type 2 Diabetes Mellitus (E11.65) - SUBOPTIMALLY CONTROLLED
   - A1c 7.6%, improved from 7.8% but above goal <7%
   - Continue Metformin 1000mg BID + 500mg daily, Glipizide 10mg BID
   - Reinforce dietary counseling, increase physical activity
   - Recheck A1c in 3 months
   - Annual diabetic foot exam performed today - NORMAL
   - Referral to ophthalmology for diabetic eye exam
   Medical Necessity: Ongoing management to prevent microvascular complications

2. Hypertensive Heart Disease without Heart Failure (I11.9) - CONTROLLED
   - BP 138/84, at goal <140/90
   - Continue Amlodipine 10mg + Losartan 100mg daily
   - Annual EKG ordered
   Medical Necessity: Chronic disease management to prevent cardiovascular events

3. Mixed Hyperlipidemia (E78.2) - AT GOAL
   - LDL 98, at goal <100 for diabetic patient
   - Continue Atorvastatin 20mg daily
   Medical Necessity: Secondary prevention in patient with diabetes and atherosclerosis

4. Chronic Gout (M1A.9) - STABLE, NO ACUTE FLARE
   - Uric acid 7.2, asymptomatic
   - Continue current management, dietary counseling
   Medical Necessity: Chronic disease monitoring

5. Anemia (D64.9) - IMPROVING
   - Hgb improved 11.2 to 12.8
   - Continue Ferrous Sulfate 325mg daily
   - Recheck CBC in 3 months
   Medical Necessity: Treatment to prevent symptoms and complications

6. Mood Disorder (F39) - STABLE
   - Continue psychiatric medications (managed by psychiatry)
   - Follow-up with psychiatry as scheduled
   Medical Necessity: Coordination of care

7. Proteinuria (R80.9) - MONITORING
   - Microalbumin/creatinine 45 mg/g, eGFR 72 (CKD Stage 2)
   - Continue Losartan for renal protection
   - Recheck in 3 months
   Medical Necessity: Early intervention to prevent diabetic nephropathy

8. Atherosclerosis of Aorta (I70.0) - STABLE
   - Asymptomatic, on statin therapy
   - Continue lifestyle modifications
   Medical Necessity: Secondary prevention

MEDICATIONS RECONCILED:
1. Metformin 1000mg PO BID - CONTINUE
2. Metformin 500mg PO daily - CONTINUE
3. Glipizide 10mg PO BID - CONTINUE
4. Amlodipine 10mg PO daily PM - CONTINUE
5. Losartan 100mg PO daily - CONTINUE
6. Atorvastatin 20mg PO daily PM - CONTINUE
7. Ferrous Sulfate 325mg PO daily - CONTINUE

Allergies: NKDA

COUNSELING PROVIDED:
- Nutrition counseling: DASH diet, carbohydrate counting, limit purine-rich foods (10 minutes)
- Physical activity counseling: goal 150 min/week moderate exercise (5 minutes)
- Medication adherence reinforced
Total Counseling Time: 15 minutes

PATIENT INSTRUCTIONS:
1. Continue all medications as prescribed
2. Monitor blood glucose and BP at home, log readings
3. Follow low-sodium, low-carbohydrate diet
4. Increase physical activity as tolerated
5. Schedule ophthalmology appointment
6. Return in 3 months or sooner if concerns

RETURN PRECAUTIONS:
Return immediately if: chest pain, severe headache, glucose >300 or <70 with symptoms, signs of infection, severe joint pain, blood in stool, shortness of breath

FOLLOW-UP: 3 months
Labs before next visit: A1c, BMP, CBC, lipid panel, urine microalbumin""",
            clinician_role="Physician",
            encounter_context="Routine chronic disease management follow-up. Multiple comorbidities including DM2, HTN, gout, anemia, hyperlipidemia. Patient transitioning insurance.",
            note_type="Progress",
            output_language="en",
            payer="Medicare",
            phi_safe_mode=True,
            setting="outpatient",
            specialty="Internal Medicine",
            time_spent_minutes=25,
        ),
    ),
    DatasetRow(
        label="NEW TEST - Back Pain & Urology Referral (Dr. Gómez)",
        inputs=Inputs(
            clinical_dictation="""Progress Note New 1/22/2024

Chief Complaint
REFERRAL TO UROLOGY FOR F/U. ALSO REFERS UPPER AND MID BACK PAIN

Present Illness
REFERRAL TO UROLOGY FOR F/U. ALSO REFERS UPPER AND MID BACK PAIN

Review of Systems
Psychiatric mood, mood swings. anxiety. insomnia.
Eyes vision loss.

Physical Exam
General Appearance oriented to alert, active and no acute distress. active. Normal. well developed.
Ears, Nose, Mouth & Throat oropharynx, oral mucosa, palates. moist oral membrane; intact pharynx. hearing. hearing grossly intact. external ears and nose. no nasal discharge. normal, no deformities or lesions. otoscopic exam. canals clear, tympanic membranes intact with good movement, no fluid. nasal mucosa, septum, and turbinates. normal mucosa, septum, and turbinates. lips, teeth, and gums. good dentition.
Respiratory respiratory effort. normal respiratory effort. auscultation. no rales, rhochi, or wheezes. palpation. normal fremitus. percussion. no dullness.
Cardiovascular auscultation. regular rate and rhythm.
Abdomen soft, nontender, bowel sounds normal, no masses.
Neurologic

Assessment
Male patient of 60 year(s) of age Comes with: REFERRAL TO UROLOGY FOR F/U. ALSO REFERS UPPER AND MID BACK PAIN
Patient now presents: F1320 sedative, hypnotic or anxiolytic dependence, uncomplicated, F39 unspecified mood [affective] disorder, J8410 pulmonary fibrosis, unspecified, M542 cervicalgia, M62838 other muscle spasm, E039 hypothyroidism, unspecified.

Active diagnosis are:
- F1320 Sedative, hypnotic or anxiolytic dependence, uncomplicated
- F39 Unspecified mood [affective] disorder
- J8410 Pulmonary fibrosis, unspecified
- E7800 Pure hypercholesterolemia, unspecified
- M542 Cervicalgia
- Z0289 Encounter for other administrative examinations
- Z760 Encounter for issue of repeat prescription
- M62838 Other muscle spasm
- M545 Low back pain
- E039 Hypothyroidism, unspecified

Vital Signs
Wt: 175 lbs. Ht: 71 inches. BMI: 24.4

Plan
Medications prescribed were:
- Nabumetone 500 mg oral tablet Take One Tab PO Q12HRS PRN FOR PAIN
- Orphenadrine Citrate 100 mg oral tablet, extended release Take One Tab PO AT NIGHT PRN
- Synthroid 100 mcg (0.1 mg) oral tablet Take One Tab PO Every Day in AM DAW1
- Maximum D3 325 mcg oral capsule Take One CAP PO QWK
- Simvastatin 20 mg oral tablet Take One Tab PO Daily in PM

Orders given were: Vitamin D, 25-Hydroxy, Comprehensive metabolic panel, PTH Intact, U/A, Hemoglobin glycosylated (A1C), Microalbumin, Occult Blood Fecal IA, PSA, CBC + differential, Lipid panel, TSH, Radiologic examination spine cervical 3 views or less, Radiologic examination spine thoracic 2 views.

Counseling for nutrition and physical activity were offered. Patient instructed to return as necessary.""",
            clinician_role="Physician",
            note_type="Progress",
            output_language="en",
            payer="Medicare",
            phi_safe_mode=True,
            setting="outpatient",
            specialty="General Practice",
        ),
    ),
    DatasetRow(
        label="ORIGINAL Note - Progress Note Med Refill (Incomplete)",
        inputs=Inputs(
            clinical_dictation="""Progress Note New 1/19/2023

Chief Complaint
med refill and change of health insurance

Present Illness
med refill and change of health insurance

Assessment
Male patient of 66 year(s) of age Comes with: med refill and change of health insurance. 
Patient now presents: Z760 encounter for issue of repeat prescription.

Active diagnosis are: 
- E11618 Type 2 diabetes mellitus with other diabetic arthropathy
- I700 Atherosclerosis of aorta
- M064 Inflammatory polyarthropathy
- F39 Unspecified mood [affective] disorder
- I119 Hypertensive heart disease without heart failure
- D649 Anemia, unspecified
- R809 Proteinuria, unspecified
- E782 Mixed hyperlipidemia
- M1A079 Idiopathic chronic gout, unspecified ankle and foot

Plan
Medications prescribed were:
- Ferrous Sulfate 325 mg oral tablet Take One Tab PO Daily
- AmLODIPine Besylate 10 mg oral tablet Take One Tab PO Daily IN PM
- MetFORMIN Hydrochloride 1000 mg oral tablet Take One Tab PO BID
- Atorvastatin Calcium 20 mg oral tablet Take One Tab PO Daily in PM
- GlipiZIDE 10 mg oral tablet Take One Tab PO BID
- MetFORMIN Hydrochloride 500 mg oral tablet Take One Tab PO Daily
- Losartan Potassium 100 mg oral tablet Take One Tab PO Daily

Counseling for nutrition and physical activity were offered. 
Patient instructed to return as necessary.""",
            clinician_role="Physician",
            note_type="Progress",
            output_language="en",
            payer="Medicare",
            phi_safe_mode=True,
            setting="outpatient",
            specialty="Internal Medicine",
        ),
    ),
    DatasetRow(
        label="SOAP - Diabetes Follow-up (Medicare)",
        inputs=Inputs(
            clinical_dictation="""Paciente masculino de 58 años con DM2 diagnosticada hace 5 años, viene para seguimiento. 
Refiere buen control glucémico en casa, glucosas en ayunas entre 110-130 mg/dL. Niega hipoglucemias. 
Adherente a metformina. Dieta variable, admite consumo ocasional de carbohidratos refinados. 
Ejercicio: camina 20 min 3x/semana. Última A1c hace 3 meses fue 7.2%.

ROS: Niega poliuria, polidipsia, visión borrosa, parestesias, dolor torácico, disnea.

PE: PA 138/82, FC 76, Peso 92kg (previo 94kg hace 3 meses). Alerta, orientado. 
Cardiopulmonar normal. Extremidades sin edema, pulsos pedios presentes bilaterales, monofilamento normal.

Labs: A1c hoy: 6.9%, Creatinina 1.0, eGFR 85, Lipidos: LDL 98, HDL 42, TG 165.

Diagnósticos: DM2, HTN, dislipidemia

Meds: Metformina 1000mg BID, Lisinopril 10mg diario, Atorvastatina 20mg diario. NKDA.

Plan: Continuar metformina, felicitar por pérdida de peso y mejora de A1c. Reforzar dieta y ejercicio. 
Aumentar lisinopril a 20mg por PA elevada. Repetir labs en 3 meses. 
Referir a oftalmología para examen anual. Vacuna influenza administrada hoy.
Counseling sobre dieta 10 minutos.""",
            clinician_role="Physician",
            note_type="SOAP",
            output_language="es",
            payer="Medicare",
            phi_safe_mode=True,
            setting="outpatient",
            specialty="Internal Medicine",
        ),
    ),
    DatasetRow(
        label="H&P - Chest Pain ED (Inpatient)",
        inputs=Inputs(
            clinical_dictation="""67 year old female with history of HTN and active smoking (1 pack/day x 40 years) 
presents with substernal chest pain onset 2 hours ago. Describes as pressure, 7/10 intensity, 
radiating to left arm, associated with diaphoresis and nausea. No relief with rest. 
No prior similar episodes.

ROS: Positive for chest pain, diaphoresis, nausea. Denies dyspnea, palpitations, syncope, abdominal pain.

PE: BP 158/94, HR 92, RR 18, SpO2 97% RA, Temp 36.8. Anxious, diaphoretic. 
Neck without JVD. Lungs clear bilateral. Heart RRR without murmurs. Abdomen soft. 
Extremities without edema, symmetric pulses.

Labs/Imaging: ECG: ST elevation 2mm in V2-V4. Troponin I: 0.8 ng/mL (normal <0.04). 
BMP normal. CBC normal. CXR: no infiltrates, normal cardiac silhouette.

Known diagnoses: HTN

Meds: Amlodipine 5mg daily (admits poor adherence). Allergies: Penicillin (rash)

Plan: STEMI anterior. Aspirin 325mg and Heparin administered. 
Cardiology called for emergent cath. Consent obtained for catheterization. NPO. Continuous monitoring.""",
            clinician_role="Physician",
            note_type="H&P",
            output_language="en",
            payer="Medicare",
            phi_safe_mode=True,
            setting="ED",
            specialty="Emergency Medicine",
            time_spent_minutes=45,
        ),
    ),
    DatasetRow(
        label="Incomplete Dictation (Should Fail)",
        inputs=Inputs(
            clinical_dictation="asdf",
            clinician_role="Physician",
            note_type="SOAP",
            output_language="en",
            phi_safe_mode=True,
            setting="outpatient",
        ),
    ),
    DatasetRow(
        label="PDF TEST - Labs Review & Hemorrhagic Conditions (Dr. Gómez)",
        inputs=Inputs(
            clinical_document=VellumDocument(
                src="https://storage.googleapis.com/vellum-public-test-files/atlas-test-note-laudelino-reyes.pdf"
            ),
            clinician_role="Physician",
            note_type="Progress",
            output_language="en",
            payer="Medicare",
            phi_safe_mode=True,
            setting="outpatient",
            specialty="General Practice",
        ),
    ),
    DatasetRow(
        label="PHI Test - Names in Dictation",
        inputs=Inputs(
            clinical_dictation="""John Smith, DOB 01/15/1960, MRN 123456789, presents for follow-up of hypertension.
Patient reports compliance with medications. BP today 128/78. 
Continue current regimen. Follow-up in 3 months.
Contact: 555-123-4567, 123 Main Street, Anytown USA.""",
            clinician_role="Physician",
            note_type="Progress",
            output_language="en",
            payer="Commercial",
            phi_safe_mode=True,
            setting="outpatient",
            specialty="Family Medicine",
        ),
    ),
]

runner = WorkflowSandboxRunner(workflow=Workflow(), dataset=dataset)

if __name__ == "__main__":
    runner.run()
