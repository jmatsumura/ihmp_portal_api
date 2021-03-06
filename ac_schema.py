import graphene
from models import Pagination, CaseHits, Aggregations
from query import get_buckets, get_case_hits, get_pagination

# Can preload counts by declaring these in this next block. 
# These aggregations can remain stagnant so don't need to update
# based on filters as these are used to give a total count of the data.

file_annotation_pipeline = get_buckets("F.annotation_pipeline","no","")
file_format = get_buckets("F.format","no","")
file_id = get_buckets("F.id","no","")
file_matrix_type = get_buckets("F.matrix_type","no","")
file_type = get_buckets("F.node_type","no","")

pro_name = get_buckets("PS.project_name","no","")
pro_subtype = get_buckets("PS.project_subtype","no","")

sam_biome = get_buckets("VSS.biome","no","")
sam_body_product = get_buckets("VSS.body_product","no","")
sam_body_site = get_buckets("VSS.body_site","no","")
sam_collection_date = get_buckets("VSS.collection_date","no","")
sam_env_package = get_buckets("VSS.env_package","no","")
sam_feature = get_buckets("VSS.feature","no","")
sam_fecalcal = get_buckets("VSS.fecalcal","no","")
sam_geo_loc_name = get_buckets("VSS.geo_loc_name","no","")
sam_id = get_buckets("VSS.id","no","")
sam_lat_lon = get_buckets("VSS.lat_lon","no","")
sam_material = get_buckets("VSS.material","no","")
sam_rel_to_oxygen = get_buckets("VSS.rel_to_oxygen","no","")
sam_samp_collect_device = get_buckets("VSS.samp_collect_device","no","")
sam_samp_mat_process = get_buckets("VSS.samp_mat_process","no","")
sam_samp_size = get_buckets("VSS.samp_size","no","")
sam_subtype = get_buckets("VSS.subtype","no","")
sam_supersite = get_buckets("VSS.supersite","no","")

stu_center = get_buckets("VSS.study_center","no","")
stu_contact = get_buckets("VSS.study_contact","no","")
stu_description = get_buckets("VSS.study_description","no","")
stu_name = get_buckets("VSS.study_name","no","")
stu_srp_id = get_buckets("VSS.study_srp_id","no","")
stu_subtype = get_buckets("VSS.study_subtype","no","")
sub_aerobics = get_buckets("PS.aerobics","no","")
sub_alcohol = get_buckets("PS.alcohol","no","")
sub_allergies = get_buckets("PS.allergies","no","")
sub_asthma = get_buckets("PS.asthma","no","")
sub_cad = get_buckets("PS.cad","no","")
sub_chf = get_buckets("PS.chf","no","")
sub_comment = get_buckets("PS.comment","no","")
sub_contact = get_buckets("PS.contact","no","")
sub_diabetes = get_buckets("PS.diabetes","no","")
sub_education = get_buckets("PS.education","no","")
sub_family_history = get_buckets("PS.family_history","no","")
sub_father = get_buckets("PS.father","no","")
sub_gallbladder = get_buckets("PS.gallbladder","no","")
sub_gender = get_buckets("PS.gender","no","")
sub_hyperlipidemia = get_buckets("PS.hyperlipidemia","no","")
sub_hypertension = get_buckets("PS.hypertension","no","")
sub_id = get_buckets("PS.rand_subject_id","no","")
sub_illicit_drug = get_buckets("PS.illicit_drug","no","")
sub_kidney = get_buckets("PS.kidney","no","")
sub_liver = get_buckets("PS.liver","no","")
sub_lmp = get_buckets("PS.lmp","no","")
sub_mother = get_buckets("PS.mother","no","")
sub_occupation = get_buckets("PS.occupation","no","")
sub_osa = get_buckets("PS.osa","no","")
sub_pancreatitis = get_buckets("PS.pancreatitis","no","")
sub_postmenopausal = get_buckets("PS.postmenopausal","no","")
sub_pvd = get_buckets("PS.pvd","no","")
sub_race = get_buckets("PS.race","no","")
sub_rx = get_buckets("PS.rx","no","")
sub_subtype = get_buckets("PS.subtype","no","")
sub_survey_id = get_buckets("PS.survey_id","no","")
sub_tobacco = get_buckets("PS.tobacco","no","")
sub_uuid = get_buckets("PS.id","no","")

tag_term = get_buckets("T.term","no","")

vis_30m_gluc = get_buckets("VSS.visit_30m_gluc","no","")
vis_60m_gluc = get_buckets("VSS.visit_60m_gluc","no","")
vis_abdominal_pain = get_buckets("VSS.visit_abdominal_pain","no","")
vis_abx = get_buckets("VSS.visit_abx","no","")
vis_activity_30d = get_buckets("VSS.visit_activity_30d","no","")
vis_activity_3m = get_buckets("VSS.visit_activity_3m","no","")
vis_activity_change_30d = get_buckets("VSS.visit_activity_change_30d","no","")
vis_activity_change_3m = get_buckets("VSS.visit_activity_change_3m","no","")
vis_acute_dis = get_buckets("VSS.visit_acute_dis","no","")
vis_age = get_buckets("VSS.visit_age","no","")
vis_alcohol = get_buckets("VSS.visit_alcohol","no","")
vis_anger = get_buckets("VSS.visit_anger","no","")
vis_arthralgia = get_buckets("VSS.visit_arthralgia","no","")
vis_beans = get_buckets("VSS.visit_beans","no","")
vis_biscuit = get_buckets("VSS.visit_biscuit","no","")
vis_bmi = get_buckets("VSS.visit_bmi","no","")
vis_bowel_day = get_buckets("VSS.visit_bowel_day","no","")
vis_bowel_night = get_buckets("VSS.visit_bowel_night","no","")
vis_bread = get_buckets("VSS.visit_bread","no","")
vis_bread_spread = get_buckets("VSS.visit_bread_spread","no","")
vis_breadrolls = get_buckets("VSS.visit_breadrolls","no","")
vis_breakfast_amt = get_buckets("VSS.visit_breakfast_amt","no","")
vis_breakfast_food = get_buckets("VSS.visit_breakfast_food","no","")
vis_breakfast_tod = get_buckets("VSS.visit_breakfast_tod","no","")
vis_cancer = get_buckets("VSS.visit_cancer","no","")
vis_cancer_mtc = get_buckets("VSS.visit_cancer_mtc","no","")
vis_cereal = get_buckets("VSS.visit_cereal","no","")
vis_cereal_type = get_buckets("VSS.visit_cereal_type","no","")
vis_cheese = get_buckets("VSS.visit_cheese","no","")
vis_chemo = get_buckets("VSS.visit_chemo","no","")
vis_chest_pain = get_buckets("VSS.visit_chest_pain","no","")
vis_chips_crisps = get_buckets("VSS.visit_chips_crisps","no","")
vis_chronic_dis = get_buckets("VSS.visit_chronic_dis","no","")
vis_claudication = get_buckets("VSS.visit_claudication","no","")
vis_colonoscopy = get_buckets("VSS.visit_colonoscopy","no","")
vis_confident = get_buckets("VSS.visit_confident","no","")
vis_control = get_buckets("VSS.visit_control","no","")
vis_coping = get_buckets("VSS.visit_coping","no","")
vis_current = get_buckets("VSS.visit_current","no","")
vis_dairy = get_buckets("VSS.visit_dairy","no","")
vis_date = get_buckets("VSS.visit_date","no","")
vis_diag_other = get_buckets("VSS.visit_diag_other","no","")
vis_diarrhea = get_buckets("VSS.visit_diarrhea","no","")
vis_diet_drinks = get_buckets("VSS.visit_diet_drinks","no","")
vis_difficulties = get_buckets("VSS.visit_difficulties","no","")
vis_dinner_amt = get_buckets("VSS.visit_dinner_amt","no","")
vis_dinner_food = get_buckets("VSS.visit_dinner_food","no","")
vis_dinner_tod = get_buckets("VSS.visit_dinner_tod","no","")
vis_duration = get_buckets("VSS.visit_duration","no","")
vis_dyspnea = get_buckets("VSS.visit_dyspnea","no","")
vis_eggs = get_buckets("VSS.visit_eggs","no","")
vis_ery_nodosum = get_buckets("VSS.visit_ery_nodosum","no","")
vis_fast_gluc = get_buckets("VSS.visit_fast_gluc","no","")
vis_fever = get_buckets("VSS.visit_fever","no","")
vis_fish = get_buckets("VSS.visit_fish","no","")
vis_fish_count = get_buckets("VSS.visit_fish_count","no","")
vis_fish_oil = get_buckets("VSS.visit_fish_oil","no","")
vis_fish_white = get_buckets("VSS.visit_fish_white","no","")
vis_fruit = get_buckets("VSS.visit_fruit","no","")
vis_fruit_count = get_buckets("VSS.visit_fruit_count","no","")
vis_going_your_way = get_buckets("VSS.visit_going_your_way","no","")
vis_grains = get_buckets("VSS.visit_grains","no","")
vis_hbi = get_buckets("VSS.visit_hbi","no","")
vis_hbi_total = get_buckets("VSS.visit_hbi_total","no","")
vis_height = get_buckets("VSS.visit_height","no","")
vis_hosp = get_buckets("VSS.visit_hosp","no","")
vis_ice_cream = get_buckets("VSS.visit_ice_cream","no","")
vis_id = get_buckets("VSS.visit_id","no","")
vis_immunosupp = get_buckets("VSS.visit_immunosupp","no","")
vis_interval = get_buckets("VSS.visit_interval","no","")
vis_irritation = get_buckets("VSS.visit_irritation","no","")
vis_juice = get_buckets("VSS.visit_juice","no","")
vis_leg_edema = get_buckets("VSS.visit_leg_edema","no","")
vis_lunch_amt = get_buckets("VSS.visit_lunch_amt","no","")
vis_lunch_food = get_buckets("VSS.visit_lunch_food","no","")
vis_lunch_tod = get_buckets("VSS.visit_lunch_tod","no","")
vis_meat = get_buckets("VSS.visit_meat","no","")
vis_meat_product = get_buckets("VSS.visit_meat_product","no","")
vis_meat_red = get_buckets("VSS.visit_meat_red","no","")
vis_meat_white = get_buckets("VSS.visit_meat_white","no","")
vis_milk = get_buckets("VSS.visit_milk","no","")
vis_mod_activity_days = get_buckets("VSS.visit_mod_activity_days","no","")
vis_mod_activity_hours = get_buckets("VSS.visit_mod_activity_hours","no","")
vis_mod_activity_minutes = get_buckets("VSS.visit_mod_activity_minutes","no","")
vis_neurologic = get_buckets("VSS.visit_neurologic","no","")
vis_new_meds = get_buckets("VSS.visit_new_meds","no","")
vis_number = get_buckets("VSS.visit_visit_number","no","")
vis_on_top = get_buckets("VSS.visit_on_top","no","")
vis_oral_contrast = get_buckets("VSS.visit_oral_contrast","no","")
vis_other_food_intake = get_buckets("VSS.visit_other_food_intake","no","")
vis_pastry = get_buckets("VSS.visit_pastry","no","")
vis_poultry = get_buckets("VSS.visit_poultry","no","")
vis_preg_plans = get_buckets("VSS.visit_preg_plans","no","")
vis_pregnant = get_buckets("VSS.visit_pregnant","no","")
vis_prior = get_buckets("VSS.visit_prior","no","")
vis_probiotic = get_buckets("VSS.visit_probiotic","no","")
vis_psychiatric = get_buckets("VSS.visit_psychiatric","no","")
vis_pyo_gangrenosum = get_buckets("VSS.visit_pyo_gangrenosum","no","")
vis_rash = get_buckets("VSS.visit_rash","no","")
vis_salt = get_buckets("VSS.visit_salt","no","")
vis_sccai = get_buckets("VSS.visit_sccai","no","")
vis_sccai_total = get_buckets("VSS.visit_sccai_total","no","")
vis_self_assess = get_buckets("VSS.visit_self_assess","no","")
vis_self_condition = get_buckets("VSS.visit_self_condition","no","")
vis_shellfish = get_buckets("VSS.visit_shellfish","no","")
vis_snacks_amt = get_buckets("VSS.visit_snacks_amt","no","")
vis_snacks_food = get_buckets("VSS.visit_snacks_food","no","")
vis_snacks_tod = get_buckets("VSS.visit_snacks_tod","no","")
vis_soda = get_buckets("VSS.visit_soda","no","")
vis_starch = get_buckets("VSS.visit_starch","no","")
vis_starch_type = get_buckets("VSS.visit_starch_type","no","")
vis_stool_blood = get_buckets("VSS.visit_stool_blood","no","")
vis_stool_soft = get_buckets("VSS.visit_stool_soft","no","")
vis_stopped_meds = get_buckets("VSS.visit_stopped_meds","no","")
vis_stress = get_buckets("VSS.visit_stress","no","")
vis_stress_def = get_buckets("VSS.visit_stress_def","no","")
vis_study_disease_comment = get_buckets("VSS.visit_study_disease_comment","no","")
vis_study_disease_description = get_buckets("VSS.visit_study_disease_description","no","")
vis_study_disease_disease_ontology_id = get_buckets("VSS.visit_study_disease_disease_ontology_id","no","")
vis_study_disease_mesh_id = get_buckets("VSS.visit_study_disease_mesh_id","no","")
vis_study_disease_name = get_buckets("VSS.visit_study_disease_name","no","")
vis_study_disease_nci_id = get_buckets("VSS.visit_study_disease_nci_id","no","")
vis_study_disease_status = get_buckets("VSS.visit_study_disease_status","no","")
vis_study_disease_umls_concept_id = get_buckets("VSS.visit_study_disease_umls_concept_id","no","")
vis_subtype = get_buckets("VSS.visit_subtype","no","")
vis_sugar = get_buckets("VSS.visit_sugar","no","")
vis_sugar_drinks = get_buckets("VSS.visit_sugar_drinks","no","")
vis_surgery = get_buckets("VSS.visit_surgery","no","")
vis_sweets = get_buckets("VSS.visit_sweets","no","")
vis_sweets_count = get_buckets("VSS.visit_sweets_count","no","")
vis_upset = get_buckets("VSS.visit_upset","no","")
vis_urgency_def = get_buckets("VSS.visit_urgency_def","no","")
vis_uveitis = get_buckets("VSS.visit_uveitis","no","")
vis_veg = get_buckets("VSS.visit_veg","no","")
vis_veg_green = get_buckets("VSS.visit_veg_green","no","")
vis_veg_raw = get_buckets("VSS.visit_veg_raw","no","")
vis_veg_root = get_buckets("VSS.visit_veg_root","no","")
vis_vig_activity_days = get_buckets("VSS.visit_vig_activity_days","no","")
vis_vig_activity_hours = get_buckets("VSS.visit_vig_activity_hours","no","")
vis_vig_activity_minutes = get_buckets("VSS.visit_vig_activity_minutes","no","")
vis_walking_days = get_buckets("VSS.visit_walking_days","no","")
vis_walking_hours = get_buckets("VSS.visit_walking_hours","no","")
vis_walking_minutes = get_buckets("VSS.visit_walking_minutes","no","")
vis_water = get_buckets("VSS.visit_water","no","")
vis_weight = get_buckets("VSS.visit_weight","no","")
vis_weight_change = get_buckets("VSS.visit_weight_change","no","")
vis_weight_diff = get_buckets("VSS.visit_weight_diff","no","")
vis_work_missed = get_buckets("VSS.visit_work_missed","no","")
vis_yogurt = get_buckets("VSS.visit_yogurt","no","")

class Query(graphene.ObjectType):

    pagination = graphene.Field(Pagination, cy=graphene.String(description='Cypher WHERE parameters'), s=graphene.Int(description='size of subset to return'), f=graphene.Int(description='what position of the sort to start at'))
    hits = graphene.List(CaseHits, cy=graphene.String(description='Cypher WHERE parameters'), s=graphene.Int(description='size of subset to return'), o=graphene.String(description='what to sort by'), f=graphene.Int(description='what position of the sort to start at'))
    aggregations = graphene.Field(Aggregations)

    def resolve_pagination(self, args, context, info):
        cy = args['cy'].replace("|",'"')
        return get_pagination(cy,args['s'],args['f'],'c')

    def resolve_hits(self, args, context, info):
        cy = args['cy'].replace("|",'"') # handle quotes for GQL
        if args['cy'] == "":
            return get_case_hits(args['s'],args['o'],args['f'],"")
        else:
            return get_case_hits(args['s'],args['o'],args['f'],cy)

    def resolve_aggregations(self, args, context, info):
        return Aggregations(
            file_annotation_pipeline=file_annotation_pipeline,
            file_format=file_format,
            file_id=file_id,
            file_matrix_type=file_matrix_type,
            file_type=file_type,
            project_name=pro_name,
            project_subtype=pro_subtype,
            sample_biome=sam_biome,
            sample_body_product=sam_body_product,
            sample_body_site=sam_body_site,
            sample_collection_date=sam_collection_date,
            sample_env_package=sam_env_package,
            sample_feature=sam_feature,
            sample_fecalcal=sam_fecalcal,
            sample_geo_loc_name=sam_geo_loc_name,
            sample_id=sam_id,
            sample_lat_lon=sam_lat_lon,
            sample_material=sam_material,
            sample_rel_to_oxygen=sam_rel_to_oxygen,
            sample_samp_collect_device=sam_samp_collect_device,
            sample_samp_mat_process=sam_samp_mat_process,
            sample_samp_size=sam_samp_size,
            sample_subtype=sam_subtype,
            sample_supersite=sam_supersite,
            study_center=stu_center,
            study_contact=stu_contact,
            study_description=stu_description,
            study_name=stu_name,
            study_srp_id=stu_srp_id,
            study_subtype=stu_subtype,
            subject_aerobics=sub_aerobics,
            subject_alcohol=sub_alcohol,
            subject_allergies=sub_allergies,
            subject_asthma=sub_asthma,
            subject_cad=sub_cad,
            subject_chf=sub_chf,
            subject_comment=sub_comment,
            subject_contact=sub_contact,
            subject_diabetes=sub_diabetes,
            subject_education=sub_education,
            subject_family_history=sub_family_history,
            subject_father=sub_father,
            subject_gallbladder=sub_gallbladder,
            subject_gender=sub_gender,
            subject_hyperlipidemia=sub_hyperlipidemia,
            subject_hypertension=sub_hypertension,
            subject_id=sub_id,
            subject_illicit_drug=sub_illicit_drug,
            subject_kidney=sub_kidney,
            subject_liver=sub_liver,
            subject_lmp=sub_lmp,
            subject_mother=sub_mother,
            subject_occupation=sub_occupation,
            subject_osa=sub_osa,
            subject_pancreatitis=sub_pancreatitis,
            subject_postmenopausal=sub_postmenopausal,
            subject_pvd=sub_pvd,
            subject_race=sub_race,
            subject_rx=sub_rx,
            subject_subtype=sub_subtype,
            subject_survey_id=sub_survey_id,
            subject_tobacco=sub_tobacco,
            subject_uuid=sub_uuid,
            tag_term=tag_term,
            visit_30m_gluc=vis_30m_gluc,
            visit_60m_gluc=vis_60m_gluc,
            visit_abdominal_pain=vis_abdominal_pain,
            visit_abx=vis_abx,
            visit_activity_30d=vis_activity_30d,
            visit_activity_3m=vis_activity_3m,
            visit_activity_change_30d=vis_activity_change_30d,
            visit_activity_change_3m=vis_activity_change_3m,
            visit_acute_dis=vis_acute_dis,
            visit_age=vis_age,
            visit_alcohol=vis_alcohol,
            visit_anger=vis_anger,
            visit_arthralgia=vis_arthralgia,
            visit_beans=vis_beans,
            visit_biscuit=vis_biscuit,
            visit_bmi=vis_bmi,
            visit_bowel_day=vis_bowel_day,
            visit_bowel_night=vis_bowel_night,
            visit_bread=vis_bread,
            visit_bread_spread=vis_bread_spread,
            visit_breadrolls=vis_breadrolls,
            visit_breakfast_amt=vis_breakfast_amt,
            visit_breakfast_food=vis_breakfast_food,
            visit_breakfast_tod=vis_breakfast_tod,
            visit_cancer=vis_cancer,
            visit_cancer_mtc=vis_cancer_mtc,
            visit_cereal=vis_cereal,
            visit_cereal_type=vis_cereal_type,
            visit_cheese=vis_cheese,
            visit_chemo=vis_chemo,
            visit_chest_pain=vis_chest_pain,
            visit_chips_crisps=vis_chips_crisps,
            visit_chronic_dis=vis_chronic_dis,
            visit_claudication=vis_claudication,
            visit_colonoscopy=vis_colonoscopy,
            visit_confident=vis_confident,
            visit_control=vis_control,
            visit_coping=vis_coping,
            visit_current=vis_current,
            visit_dairy=vis_dairy,
            visit_date=vis_date,
            visit_diag_other=vis_diag_other,
            visit_diarrhea=vis_diarrhea,
            visit_diet_drinks=vis_diet_drinks,
            visit_difficulties=vis_difficulties,
            visit_dinner_amt=vis_dinner_amt,
            visit_dinner_food=vis_dinner_food,
            visit_dinner_tod=vis_dinner_tod,
            visit_duration=vis_duration,
            visit_dyspnea=vis_dyspnea,
            visit_eggs=vis_eggs,
            visit_ery_nodosum=vis_ery_nodosum,
            visit_fast_gluc=vis_fast_gluc,
            visit_fever=vis_fever,
            visit_fish=vis_fish,
            visit_fish_count=vis_fish_count,
            visit_fish_oil=vis_fish_oil,
            visit_fish_white=vis_fish_white,
            visit_fruit=vis_fruit,
            visit_fruit_count=vis_fruit_count,
            visit_going_your_way=vis_going_your_way,
            visit_grains=vis_grains,
            visit_hbi=vis_hbi,
            visit_hbi_total=vis_hbi_total,
            visit_height=vis_height,
            visit_hosp=vis_hosp,
            visit_ice_cream=vis_ice_cream,
            visit_id=vis_id,
            visit_immunosupp=vis_immunosupp,
            visit_interval=vis_interval,
            visit_irritation=vis_irritation,
            visit_juice=vis_juice,
            visit_leg_edema=vis_leg_edema,
            visit_lunch_amt=vis_lunch_amt,
            visit_lunch_food=vis_lunch_food,
            visit_lunch_tod=vis_lunch_tod,
            visit_meat=vis_meat,
            visit_meat_product=vis_meat_product,
            visit_meat_red=vis_meat_red,
            visit_meat_white=vis_meat_white,
            visit_milk=vis_milk,
            visit_mod_activity_days=vis_mod_activity_days,
            visit_mod_activity_hours=vis_mod_activity_hours,
            visit_mod_activity_minutes=vis_mod_activity_minutes,
            visit_neurologic=vis_neurologic,
            visit_new_meds=vis_new_meds,
            visit_number=vis_number,
            visit_on_top=vis_on_top,
            visit_oral_contrast=vis_oral_contrast,
            visit_other_food_intake=vis_other_food_intake,
            visit_pastry=vis_pastry,
            visit_poultry=vis_poultry,
            visit_preg_plans=vis_preg_plans,
            visit_pregnant=vis_pregnant,
            visit_prior=vis_prior,
            visit_probiotic=vis_probiotic,
            visit_psychiatric=vis_psychiatric,
            visit_pyo_gangrenosum=vis_pyo_gangrenosum,
            visit_rash=vis_rash,
            visit_salt=vis_salt,
            visit_sccai=vis_sccai,
            visit_sccai_total=vis_sccai_total,
            visit_self_assess=vis_self_assess,
            visit_self_condition=vis_self_condition,
            visit_shellfish=vis_shellfish,
            visit_snacks_amt=vis_snacks_amt,
            visit_snacks_food=vis_snacks_food,
            visit_snacks_tod=vis_snacks_tod,
            visit_soda=vis_soda,
            visit_starch=vis_starch,
            visit_starch_type=vis_starch_type,
            visit_stool_blood=vis_stool_blood,
            visit_stool_soft=vis_stool_soft,
            visit_stopped_meds=vis_stopped_meds,
            visit_stress=vis_stress,
            visit_stress_def=vis_stress_def,
            visit_study_disease_comment=vis_study_disease_comment,
            visit_study_disease_description=vis_study_disease_description,
            visit_study_disease_disease_ontology_id=vis_study_disease_disease_ontology_id,
            visit_study_disease_mesh_id=vis_study_disease_mesh_id,
            visit_study_disease_name=vis_study_disease_name,
            visit_study_disease_nci_id=vis_study_disease_nci_id,
            visit_study_disease_status=vis_study_disease_status,
            visit_study_disease_umls_concept_id=vis_study_disease_umls_concept_id,
            visit_subtype=vis_subtype,
            visit_sugar=vis_sugar,
            visit_sugar_drinks=vis_sugar_drinks,
            visit_surgery=vis_surgery,
            visit_sweets=vis_sweets,
            visit_sweets_count=vis_sweets_count,
            visit_upset=vis_upset,
            visit_urgency_def=vis_urgency_def,
            visit_uveitis=vis_uveitis,
            visit_veg=vis_veg,
            visit_veg_green=vis_veg_green,
            visit_veg_raw=vis_veg_raw,
            visit_veg_root=vis_veg_root,
            visit_vig_activity_days=vis_vig_activity_days,
            visit_vig_activity_hours=vis_vig_activity_hours,
            visit_vig_activity_minutes=vis_vig_activity_minutes,
            visit_walking_days=vis_walking_days,
            visit_walking_hours=vis_walking_hours,
            visit_walking_minutes=vis_walking_minutes,
            visit_water=vis_water,
            visit_weight=vis_weight,
            visit_weight_change=vis_weight_change,
            visit_weight_diff=vis_weight_diff,
            visit_work_missed=vis_work_missed,
            visit_yogurt=vis_yogurt
            )
        
ac_schema = graphene.Schema(query=Query)