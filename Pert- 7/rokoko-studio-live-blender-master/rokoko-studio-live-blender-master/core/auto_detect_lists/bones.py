from collections import OrderedDict


ignore_rokoko_retargeting_bones = [
    'newton',
    'HeadVertex',
    'Props_LeftArm',
    'Props_RightArm',
    'LeftToeTip',
    'RightToeTip',
    'LeftFinger2Metacarpal',
    'LeftFinger3Metacarpal',
    'LeftFinger4Metacarpal',
    'LeftFinger5Metacarpal',
    'RightFinger1Tip',
    'RightFinger2Metacarpal',
    'RightFinger2Tip',
    'RightFinger3Metacarpal',
    'RightFinger3Tip',
    'RightFinger4Metacarpal',
    'RightFinger4Tip',
    'RightFinger5Metacarpal',
    'RightFinger5Tip',
]

################################
# Replace '-' with '_'
# Replace ' ' with '_'
# Replace 'ValveBiped_' with ''
# Replace 'Bip01_' with 'Bip'
# Replace 'Bip001_' with 'Bip'
#
# Replace Bone Patterns:
#   Left/Right = \L
#   L/R = \L
################################

bone_list = OrderedDict()
bone_list['hip'] = [
    'Hip',
    'Hips',
    'LowerBody',
    'Lower_Body',
    'Mixamorig:Hips',
    'Pelvis',
    'B_C_Pelvis',
    'Bip_Pelvis',
    'Hips_Root',
    'Rot_Root',
    'Sk',
    'C_Waist_1',
    'Pelwas_001',
    'Waist',
    'HipN',
    'Unused_Root_Hips',
    'Waist01',
    'Waist02',
    'Hips_Root_1',
    'Hips_Root_2',
    'Pelvis_Def',
    'J_Kosi',
    'Kosi',
    'HipMaster_01',
    'J_Bip_C_Hips',
    'J_Hip',
    'Pelvis_L',
    'Pelvis_R',
    'Root_Pelvis_1',
    'Root_X',
    # 'Root',
]
bone_list['spine'] = [  # This is a list of all spine and chest bones
    'Spine',  # First entry!

    # MMD
    'UpperBody',
    'Upper_Body',
    'Upper_Waist',
    'UpperBody2',
    'Upper_Body_2',
    'Upper_Waist_2',
    'Waist_Upper_2',
    'UpperBody3',
    'Upper_Body_3',
    'Upper_Waist_3',
    'Waist_Upper_3',

    # Mixamo
    'Mixamorig:Spine',
    'Mixamorig:Spine0',
    'Mixamorig:Spine1',
    'Mixamorig:Spine2',
    'Mixamorig:Spine3',
    'Mixamorig:Spine4',

    # 3DMax?
    'Bip_Spine',
    'Bip_Spine0',
    'Bip_Spine1',
    'Bip_Spine2',
    'Bip_Spine3',
    'Bip_Spine4',
    'Bip_Spine5',
    'Bip_Spine00',
    'Bip_Spine01',
    'Bip_Spine02',
    'Bip_Spine03',
    'Bip_Spine04',
    'Bip_Spine05',
    'Bip_Spine_0',
    'Bip_Spine_1',
    'Bip_Spine_2',
    'Bip_Spine_3',
    'Bip_Spine_4',
    'Bip_Spine_5',
    'Bip_Chest',

    # Something
    'B_C_Spine',
    'B_C_Spine0',
    'B_C_Spine1',
    'B_C_Spine2',
    'B_C_Spine3',
    'B_C_Spine4',
    'B_C_Spine5',
    'B_C_Chest',

    # .Mesh
    'Spine_Lower',
    'Spine_Lower_1',
    'Spine_Lower_2',
    'Spine_Middle',
    'Spine_Upper',
    'Spine_Upper_1',
    'Spine_Upper_2',

    'Abdomen',

    'Spine0',
    'Spine1',
    'Spine2',
    'Spine3',
    'Spine4',
    'Spine5',

    'Spine_0',
    'Spine_1',
    'Spine_2',
    'Spine_3',
    'Spine_4',
    'Spine_5',

    'Spine01',
    'Spine02',
    'Spine03',
    'Spine04',
    'Spine05',

    'Spine_01',
    'Spine_02',
    'Spine_03',
    'Spine_04',
    'Spine_05',

    'Spine_A',
    'Spine_B',
    'Spine_C',
    'Spine_D',
    'Spine_E',

    'Spine_001',
    'Spine_002',
    'Spine_003',

    'Spina00',
    'Spina01',
    'Spina02',

    'J_Spine1',
    'J_Spine2',
    'J_Spine3',

    'Spine_Jnt_01',
    'Spine_Jnt_02',
    'Spine_Jnt_03',

    'Chest1',
    'Chest2',
    'Chest3',

    'Chest_A',
    'Chest_B',
    'Chest_C',
    'Chest_D',
    'Chest_E',

    'C_Spine_A_1',
    'C_Spine_B_1',

    'J_Bip_C_Spine',
    'J_Bip_C_Chest',
    'J_Bip_C_UpperChest',

    'Pelwas',
    'Pelwas2',
    'Ribs',

    'BODY1',
    'BODY2',

    'WaistN',
    'BustN',

    'Middle',
    'Bust',

    'SpA',
    'SpB',
    'SpC',

    'Stomach_Def',
    'Chest_Def',

    'TorsoA_01',
    'TorsoB_01',
    'TorsoC_01',

    'Torso_1',
    'Torso_2',

    'AbdomenUpper',
    'ChestLower',

    'Spine_01_X',
    'Spine_02_X',

    'J_Sebo_A',
    'J_Sebo_B',
    'J_Sebo_C',

    'Mune',

    'SpineTop',

    'UpperBodyx2',

    'Chest',

    'Upper_Chest'  # Last entry!
]
bone_list['neck'] = [
    'Neck',
    'Mixamorig:Neck',
    'Head_Neck_Lower',
    'Head_Neck_Lower_1',
    'Head_Neck_Lower_2',
    'Head_Neck_Middle',
    'Bip_Neck',
    'Bip_Neck1',
    'B_C_Neck1',
    'Head_Neck',
    'J_Bip_C_Neck',
    'C_Neck_1',
    'NeckN',
    'Helmet_Lower',
    'Neck_Dev',
    'Neck00',
    'Kubi',
    'J_Kubi',
    'NeckA_01',
    'J_Neck1',
    'NeckLower',
    'Neck_X',
    'Spine_004',
]
bone_list['head'] = [
    'Head',
    'Mixamorig:Head',
    'Head_Neck_Upper',
    'Head_Neck_Upper_1',
    'Head_Neck_Upper_2',
    'Bip_Head',
    'Bip_Head1',
    'B_C_Head',
    'J_Bip_C_Head',
    'C_Head_1',
    'HeadN',
    'Helmet_Upper',
    'Head_01',
    'Head_001',
    'J_Head',
    'Head_X',
    'J_Kao',
    'Spine_005',
]
bone_list['leftShoulder'] = [
    '\L_Shoulder',
    'Shoulder_\L',
    '\LShoulder',
    '\LShoulderN',
    'Shoulder\L',
    'Mixamorig:\LShoulder',
    'Arm_\L_Shoulder',
    'Arm_\L_Shoulder_1',
    'ShoulderArm_\L',
    'Bip_\L_Clavicle',
    'Bip_Collar_\L',
    'B_\L_Shoulder',
    '\LCollar',
    '\L_Clavicle',
    '\L_Clavicle1',
    '\L_Collar',
    '\L_Clavicle_1',
    '\L_CBONE',
    'Shoulder+_\L',
    'Shol_\L',
    '\Lf_Clavicle',
    'Clavicle_\L',
    'Arm_\L_Sh_1',
    'Shoulder(\L)_0',
    '\L_Kata',
    'Cf_D_Shoulder_\L',
    'Cf_D_Shoulder2_\L',
    'Clavicle\LT_01',
    'J_Bip_\L_Shoulder',
    'J_\L_Collar',
    'J_\L_Shoulder',
    'Clavicle\L',
    'Bip_Clavicle_\L',
    '\L_Clavic',
    'J_Sako_\L',
    '\L_ShoulderPad',
    'Collarbone_\L',
]
bone_list['leftUpperArm'] = [
    '\L_Arm',
    '\LArm',
    'Arm_\L',
    '\LArmA',
    'ArmTC_\L',
    '+_\L_Elbow_Support',
    'Mixamorig:\LArm',
    'Arm_\L_Shoulder_2',
    'Bip_\L_UpperArm',
    'Bip_UpperArm_\L',
    'B_\L_Arm1',
    'Upper_Arm_\L',
    'UpperArm_\L',
    '\L_Upper_Arm',
    '\LShldr',
    '\L_UpperArm',
    '\LUpArm',
    'Uparm_\L',
    '\L_Uparm',
    '\L_Arm_01',
    'Arm_\L_Arm',
    '\L_Upperarm_1',
    'ArmFor_Correction_\L',
    '\L_ARM1',
    'Arm\L1',
    '\LShoulderJ',
    '\Lf_Shoulder',
    'Arm_Upper_\L',
    'Arm_\L_Sh_2',
    '\Larm1',
    'Shoulder(\L)_1',
    '\L_Ude',
    'Shoulder\LT_01',
    'J_Bip_\L_UpperArm',
    'J_\L_UpArm',
    'J_\L_Elbow',
    'Arm_1_\L',
    'Upperarm01_\L',
    '\L_Shldr',
    '\LShldrBend',
    'Arm_Stretch_\L',
    'J_Ude_A_\L',
    '\LShoulder',
]
bone_list['leftLowerArm'] = [
    '\L_Elbow',
    '\LElbow',
    'Elbow_\L',
    'Mixamorig:\LForeArm',
    'Arm_\L_Elbow',
    'Bip_\L_ForeArm',
    'Bip_LowerArm_\L',
    'B_\L_Arm2',
    'Fore_Arm_\L',
    'ForeArm_\L',
    '\LForeArm',
    '\L_ForeArm',
    '\LLowArm',
    '\L_Foarm',
    'Loarm_\L',
    '\L_Arm_02',
    '\L_Forearm_1',
    'Lower_Arm_\L',
    'ElbowFor_Correction_\L',
    '\L_ARM2',
    'Arm\L2',
    '\LArmJ',
    'Elb_\L',
    'Arm_\L_Elbow_1',
    'LowerArm_\L',
    '\Lf_Elbow',
    'Arm_Lower_\L',
    '\L_Forarm',
    '\Larm2',
    'Hand(\L)07',
    'Lowarm_\L',
    '\L_Hiji',
    'Elbow\LT_01',
    'J_Bip_\L_LowerArm',
    'J_\L_ForeArm',
    'Arm_2_\L',
    'Bip_Forearm_\L',
    'Lowerarm01_\L',
    '\LForearmBend',
    'Forearm_Stretch_\L',
    'J_Ude_B_\L',
]
bone_list['leftHand'] = [
    '\L_Wrist',
    '\LWrist',
    'Wrist_\L',
    'Wrist2_\L',
    'HandAux2_\L',
    'Mixamorig:\LHand',
    'Arm_\L_Wrist',
    'Arm_\L_Wirst',
    'Bip_\L_Hand',
    'Bip_Hand_\L',
    'B_\L_Hand',
    'Hand_\L',
    'Hand\L',
    '\LHand',
    '\LHandN',
    '\L_Hand',
    '\L_Hand_1',
    '\LFingerBaseN',
    '\Lf_Wrist',
    'Palm_\L',
    'Hand(\L)00',
    '\L_Te',
    'Hand\LT_01',
    'J_Bip_\L_Hand',
    'J_\L_Wrist',
    'J_Te_\L'
]
bone_list['leftUpLeg'] = [
    'Mixamorig:\LUpLeg',
    'Upper_Leg_\L',
    '\LUpLeg',
    'Upleg_\L',
    'UpperLeg_\L',
    '\L_UpLeg',
    'J_Bip_\L_UpperLeg',
    'J_\L_UpLeg',
    'Upperleg01_\L',
    '\LHip',
    '\L_Hip',
    '\L_Leg',
    '\L_Foot',
    '\LLeg',
    'Leg_\L',
    'Leg_\L_001',
    'Leg\L1',
    'LegWAux_\L',
    'Leg00003333_\L',
    'Leg00004444_\L',
    'Leg_\L_Thigh',
    'Bip_\L_Thigh',
    'Bip_Hip_\L',
    'B_\L_Leg1',
    '\LThigh',
    'Thigh_\L',
    '\L_Thigh',
    '\L_Leg_01',
    '\L_Femur',
    'Waist_Cancel_\L',
    'Waist_Cancellation_\L',
    '\L_Femur_1',
    '\L_LEG1',
    '\LLegJ',
    'Tg_\L',
    'Leg_\L_Thigh_1',
    '\Lf_Leg',
    'Thigh00_\L',
    '\Lfoot1',
    'Leg(\L)04',
    '\L_Momo',
    'Leg_Thigh_\L',
    'Hip\LT_01',
    'Leg\L',
    'Leg_1_\L',
    'Bip_Thigh_\L',
    'Groin_\L',
    '\LThighBend',
    'Thigh_Stretch_\L',
    'J_Asi_A_\L'
]
bone_list['leftLeg'] = [
    '\L_Knee',
    '\LKnee',
    'Knee_\L_001',
    'Knee_\L',
    'Mixamorig:\LLeg',
    'Leg_\L_Knee',
    'Bip_\L_Calf',
    'Bip_Knee_\L',
    'B_\L_Leg2',
    'Lower_Leg_\L',
    '\LLeg',
    '\LShin',
    'Shin_\L',
    '\L_Calf',
    'Calf_\L',
    '\LLowLeg',
    '\L_Shin',
    'Loleg_\L',
    '\L_Leg_02',
    '\L_KneeLower',
    'Tibia_\L',
    '\L_Tibia',
    '\L_Tibia_1',
    '\L_LEG2',
    'Leg\L2',
    '\LKneeJ',
    'LowerLeg_\L',
    '\Lf_Knee',
    'Leg01_\L',
    '\Lfoot2',
    'Leg(\L)00',
    '\L_Sune',
    'Leg_Calf_\L',
    'Knee\LT_01',
    'J_Bip_\L_LowerLeg',
    'J_\L_Leg',
    'Knee\L',
    'Leg_2_\L',
    'Bip_Leg_\L',
    'Lowerleg01_\L',
    'Leg_Stretch_\L',
    'J_Asi_B_\L',
]
bone_list['leftFoot'] = [
    '\L_Ankle',
    '\L_Ankle_001',
    'Ankle_\L',
    'Mixamorig:\LFoot',
    'Leg_\L_Ankle',
    'Eg_\L_Ankle',
    'Bip_\L_Foot',
    'Bip_Foot_\L',
    'B_\L_Foot',
    'Lower',
    '\LFoot',
    'Foot_\L',
    'Foot\L',
    '\L_Foot',
    'Leg_\L_Foot',
    '\L_Foot_01',
    'LegIK_\L',
    '\L_Foot_1',
    '\L_FOOT1',
    '\LFootJ',
    '\Lf_Ankle',
    '\L_Heel',
    'Leg(\L)02',
    '\L_Asi',
    'Foot\LT_01',
    'J_Bip_\L_Foot',
    'J_\L_Foot',
    '\LAnkle',
    'J_Asi_D_\L',
]
bone_list['leftToe'] = [
    '\L_Toe',
    '\L_Toes',
    '\LToe',
    '\LToe1',
    'LegTip_\L',
    'LegTipEX_\L',
    'ClawTipEX_\L',
    'Mixamorig:\LToeBase',
    'Leg_\L_Toes',
    'Bip_\L_Toe0',
    'B_\L_Toe',
    'Toe_\L',
    'Toe\L',
    '\L_Toe1',
    '\L_Toe2',
    '\LToeBase',
    'Toe1_1_\L',
    'Leg_\L_Foot_Toes',
    'ToeSaki_\L',
    '\L_Toe0',
    '\L_Toe_1',
    '\L_FOOT2',
    '\LToeN',
    '\LToeA',
    'Toes_\L',
    'ToeTip_\L',
    'ToeTip2_\L',
    '\Lf_Toe',
    'Tsumasaki_\L',
    'Leg_\L_Toe',
    'Leg(\L)03',
    'Toe\LT_01',
    'J_Bip_\L_ToeBase',
    'J_\L_Toe',
    'Bip_Toe_\L',
    'Toe_Boot_\L',
    'Toes_01_\L',
    'J_Asi_E_\L',
]

bone_list['leftThumbProximal'] = [
    'Thumb0_\L',
    '\LThumb1',
    '\LThumb1N',
    'Thumb_01_\L',
    '\L_Thumb0',
    '\L_Thumb_01',
    '\LHandThumb1',
    '\LFinger0',
    'Finger1_2_\L',
    'H_\L_Thumb1',
    'Bip_Thumb_0_\L',
    'Bip_\L_Finger0',
    '\L_Fing1_A',
    '\L_Thumb_A',
    '\L_Thumb_A_1',
    'T1_\L',
    'L_FINGER11',
    'Thumb1\L',
    'ThmbA_\L',
    '\Lf_Thumb1',
    '\L_Finger_A1',
    'Thumb01_\L',
    'Arm_\L_Finger_1_1',
    '\L_Thumbfinger_A',
    'ThumbA\LT_01',
    'J_Bip_\L_Thumb1',
    'Bip_FThumb01_\L',
    'Arm_\L_Finger_1a',
    'J_Oya_A_\L',
    '\LFinger1Metacarpal',
    'Mixamorig:\LHandThumb1',
]
bone_list['leftThumbMedial'] = [
    'Thumb1_\L',
    '\LThumb2',
    '\LThumb2N',
    'Thumb_02_\L',
    '\L_Thumb1',
    '\L_Thumb_02',
    '\LHandThumb2',
    '\LFinger01',
    'Finger1_3_\L',
    'H_\L_Thumb2',
    'Bip_Thumb_1_\L',
    'Bip_\L_Finger01',
    '\L_Fing1_B',
    '\L_Thumb_B',
    '\L_Thumb_B_1',
    'T2_\L',
    'L_FINGER12',
    'Thumb2\L',
    'ThmbB_\L',
    '\Lf_Thumb2',
    '\L_Finger_A2',
    'Thumb02_\L',
    'Arm_\L_Finger_1_2',
    '\L_Thumbfinger_B',
    'ThumbB\LT_01',
    'J_Bip_\L_Thumb2',
    'Bip_FThumb02_\L',
    'Arm_\L_Finger_1b',
    'J_Oya_B_\L',
    '\LFinger1Proximal',
    'Mixamorig:\LHandThumb2',
]
bone_list['leftThumbDistal'] = [
    'Thumb2_\L',
    '\LThumb3',
    '\LThumb3N',
    'Thumb_03_\L',
    '\L_Thumb2',
    '\L_Thumb_03',
    '\LHandThumb3',
    '\LFinger02',
    'Finger1_4_\L',
    'H_\L_Thumb3',
    'Bip_Thumb_2_\L',
    'Bip_\L_Finger02',
    '\L_Fing1_C',
    '\L_Thumb_C',
    '\L_Thumb_C_1',
    'T3_\L',
    'L_FINGER13',
    'Thumb3\L',
    'ThmbC_\L',
    '\Lf_Thumb3',
    '\L_Finger_A3',
    'Thumb03_\L',
    'Arm_\L_Finger_1_3',
    '\L_Thumbfinger_C',
    'ThumbC\LT_01',
    'J_Bip_\L_Thumb3',
    'Bip_FThumb03_\L',
    'Arm_\L_Finger_1c',
    'J_Oya_C_\L',
    '\LFinger1Distal',
    'Mixamorig:\LHandThumb3',
]
bone_list['leftIndexProximal'] = [
    'IndexFinger1_\L',
    'Fore1_\L',
    '\LIndex1',
    '\LIndex1N',
    'F_Index_01_\L',
    '\L_Index0',
    '\L_Index_01',
    '\LHandIndex1',
    '\LFinger1',
    'Finger2_2_\L',
    'H_\L_Index1',
    'Bip_Index_0_\L',
    'Bip_\L_Finger1',
    '\L_Fing2_A',
    '\L_Index_A',
    '\L_Index_A_1',
    'If1_\L',
    'L_FINGER21',
    'IndexFinger1\L',
    '\LFingerD1',
    'IndeA_\L',
    'Index1_\L',
    '\Lf_Index1',
    '\L_Finger_B1',
    'Index01_\L',
    'Arm_\L_Finger_2_1',
    '\L_Indexfinger_A',
    'IndexA\LT_01',
    'J_Bip_\L_Index1',
    'Bip_FIndex00_\L',
    'Arm_\L_Finger_2a',
    'J_Hito_A_\L',
    '\LFinger2Proximal',
    'Mixamorig:\LHandIndex1',
]
bone_list['leftIndexMedial'] = [
    'IndexFinger2_\L',
    'Fore2_\L',
    '\LIndex2',
    '\LIndex2N',
    'F_Index_02_\L',
    '\L_Index1',
    '\L_Index_02',
    '\LHandIndex2',
    '\LFinger11',
    'Finger2_3_\L',
    'H_\L_Index2',
    'Bip_Index_1_\L',
    'Bip_\L_Finger11',
    '\L_Fing2_B',
    '\L_Index_B',
    '\L_Index_B_1',
    'If2_\L',
    'L_FINGER22',
    'IndexFinger2\L',
    '\LFingerD2',
    'IndeB_\L',
    'Index2_\L',
    '\Lf_Index2',
    'Index_02_\L',
    '\L_Finger_B2',
    'Arm_\L_Finger_2_2',
    '\L_Indexfinger_B',
    'IndexB\LT_01',
    'J_Bip_\L_Index2',
    'Bip_FIndex01_\L',
    'Arm_\L_Finger_2b',
    'J_Hito_B_\L',
    '\LFinger2Medial',
    'Mixamorig:\LHandIndex2',
]
bone_list['leftIndexDistal'] = [
    'IndexFinger3_\L',
    'Fore3_\L',
    '\LIndex3',
    '\LIndex3N',
    'F_Index_03_\L',
    '\L_Index2',
    '\L_Index_03',
    '\LHandIndex3',
    '\LFinger12',
    'Finger2_4_\L',
    'H_\L_Index3',
    'Bip_Index_2_\L',
    'Bip_\L_Finger12',
    '\L_Fing2_C',
    '\L_Index_C',
    '\L_Index_C_1',
    'If3_\L',
    'L_FINGER23',
    'IndexFinger3\L',
    '\LFingerD3',
    'IndeC_\L',
    'Index3_\L',
    '\Lf_Index3',
    'Index_03_\L',
    '\L_Finger_B3',
    'Index03_\L',
    'Arm_\L_Finger_2_3',
    '\L_Indexfinger_C',
    'IndexC\LT_01',
    'J_Bip_\L_Index3',
    'Bip_FIndex02_\L',
    'Arm_\L_Finger_2c',
    'J_Hito_C_\L',
    '\LFinger2Distal',
    'Mixamorig:\LHandIndex3',
]
bone_list['leftMiddleProximal'] = [
    'MiddleFinger1_\L',
    'Middle1_\L',
    '\LMid1',
    '\LMiddle1N',
    'F_Middle_01_\L',
    '\L_Mid0',
    '\L_Middle_01',
    '\L_Middle1',
    '\LHandMiddle1',
    '\LFinger2',
    'Finger3_2_\L',
    'H_\L_Middle1',
    'Bip_Middle_0_\L',
    'Bip_\L_Finger2',
    '\L_Fing3_A',
    '\L_Middle_A',
    '\L_Middle_A_1',
    'Mf1_\L',
    'L_FINGER31',
    'MiddleFinger1\L',
    '\LFingerC1',
    'MiddA_\L',
    '\Lf_Middle1',
    'Middle_01_\L',
    '\L_Finger_C1',
    'Middle01_\L',
    'Arm_\L_Finger_3_1',
    '\L_Middlefinger_A',
    'FingerA\LT_01',
    'J_Bip_\L_Middle1',
    'Bip_FMiddle00_\L',
    'Arm_\L_Finger_3a',
    'J_Naka_A_\L',
    '\LFinger3Proximal',
    'Mixamorig:\LHandMiddle1',
]
bone_list['leftMiddleMedial'] = [
    'MiddleFinger2_\L',
    'Middle2_\L',
    '\LMid2',
    '\LMiddle2N',
    'F_Middle_02_\L',
    '\L_Mid1',
    '\L_Middle_02',
    '\L_Middle2',
    '\LHandMiddle2',
    '\LFinger21',
    'Finger3_3_\L',
    'H_\L_Middle2',
    'Bip_Middle_1_\L',
    'Bip_\L_Finger21',
    '\L_Fing3_B',
    '\L_Middle_B',
    '\L_Middle_B_1',
    'Mf2_\L',
    'L_FINGER32',
    'MiddleFinger2\L',
    '\LFingerC2',
    'MiddB_\L',
    '\Lf_Middle2',
    'Middle_02_\L',
    '\L_Finger_C2',
    'Middle02_\L',
    'Arm_\L_Finger_3_2',
    '\L_Middlefinger_B',
    'J_Bip_\L_Middle2',
    'Bip_FMiddle01_\L',
    'Arm_\L_Finger_3b',
    'J_Naka_B_\L',
    '\LFinger3Medial',
    'Mixamorig:\LHandMiddle2',
]
bone_list['leftMiddleDistal'] = [
    'MiddleFinger3_\L',
    'Middle3_\L',
    '\LMid3',
    '\LMiddle3N',
    'F_Middle_03_\L',
    '\L_Mid2',
    '\L_Middle_03',
    '\LHandMiddle3',
    '\LFinger22',
    'Finger3_4_\L',
    'H_\L_Middle3',
    'Bip_Middle_2_\L',
    'Bip_\L_Finger22',
    '\L_Fing3_C',
    '\L_Middle_C',
    '\L_Middle_C_1',
    'Mf3_\L',
    'L_FINGER33',
    'MiddleFinger3\L',
    '\LFingerC3',
    'MiddC_\L',
    '\Lf_Middle3',
    'Middle_03_\L',
    '\L_Finger_C3',
    'Middle03_\L',
    'Arm_\L_Finger_3_3',
    '\L_Middlefinger_C',
    'FingerC\LT_01',
    'J_Bip_\L_Middle3',
    'Bip_FMiddle02_\L',
    'Arm_\L_Finger_3c',
    'J_Naka_C_\L',
    '\LFinger3Distal',
    'Mixamorig:\LHandMiddle3',
]
bone_list['leftRingProximal'] = [
    'RingFinger1_\L',
    'Third1_\L',
    '\LRing1',
    '\LRing1N',
    'F_Ring_01_\L',
    '\L_Ring0',
    '\L_Ring_01',
    '\LHandRing1',
    '\LFinger3',
    'Finger4_2_\L',
    'H_\L_Ring1',
    'Bip_Ring_0_\L',
    'Bip_\L_Finger3',
    '\L_Fing4_A',
    '\L_Third_A',
    '\L_Third_A_1',
    'Rf1_\L',
    'L_FINGER41',
    'ThirdFinger1\L',
    '\LFingerB1',
    'RingA_\L',
    'Ring1_\L',
    '\Lf_Ring1',
    'Ring_01_\L',
    '\L_Finger_D1',
    'Ring01_\L',
    'Arm_\L_Finger_4_1',
    '\L_Ringfinger_A',
    'RingA\LT_01',
    'J_Bip_\L_Ring1',
    'Bip_FRing00_\L',
    'Arm_\L_Finger_4a',
    'J_Kusu_A_\L',
    '\LFinger4Proximal',
    'Mixamorig:\LHandRing1',
]
bone_list['leftRingMedial'] = [
    'RingFinger2_\L',
    'Third2_\L',
    '\LRing2',
    '\LRing2N',
    'F_Ring_02_\L',
    '\L_Ring1',
    '\L_Ring_02',
    '\LHandRing2',
    '\LFinger31',
    'Finger4_3_\L',
    'H_\L_Ring2',
    'Bip_Ring_1_\L',
    'Bip_\L_Finger31',
    '\L_Fing4_B',
    '\L_Third_B',
    '\L_Third_B_1',
    'Rf2_\L',
    'L_FINGER42',
    'ThirdFinger2\L',
    '\LFingerB2',
    'RingB_\L',
    'Ring2_\L',
    '\Lf_Ring2',
    'Ring_02_\L',
    '\L_Finger_D2',
    'Ring02_\L',
    'Arm_\L_Finger_4_2',
    '\L_Ringfinger_B',
    'RingB\LT_01',
    'J_Bip_\L_Ring2',
    'Bip_FRing01_\L',
    'Arm_\L_Finger_4b',
    'J_Kusu_B_\L',
    '\LFinger4Medial',
    'Mixamorig:\LHandRing2',
]
bone_list['leftRingDistal'] = [
    'RingFinger3_\L',
    'Third3_\L',
    '\LRing3',
    '\LRing3N',
    'F_Ring_03_\L',
    '\L_Ring2',
    '\L_Ring_03',
    '\LHandRing3',
    '\LFinger32',
    'Finger4_4_\L',
    'H_\L_Ring3',
    'Bip_Ring_2_\L',
    'Bip_\L_Finger32',
    '\L_Fing4_C',
    '\L_Third_C',
    '\L_Third_C_1',
    'Rf3_\L',
    'L_FINGER43',
    'ThirdFinger3\L',
    '\LFingerB3',
    'RingC_\L',
    'Ring3_\L',
    '\Lf_Ring3',
    'Ring_03_\L',
    '\L_Finger_D3',
    'Ring03_\L',
    'Arm_\L_Finger_4_3',
    '\L_Ringfinger_C',
    'RingC\LT_01',
    'J_Bip_\L_Ring3',
    'Bip_FRing02_\L',
    'Arm_\L_Finger_4c',
    'J_Kusu_C_\L',
    '\LFinger4Distal',
    'Mixamorig:\LHandRing3',
]
bone_list['leftLittleProximal'] = [
    'LittleFinger1_\L',
    'Little1_\L',
    '\LPinky1',
    '\LPinky1N',
    '\LLittle1N',
    'F_Pinky_01_\L',
    '\L_Pinky0',
    '\L_Pinkey_01',
    '\LHandPinky1',
    '\LFinger4',
    'Finger5_2_\L',
    'H_\L_Pinky1',
    'Bip_Pinky_0_\L',
    'Bip_\L_Finger4',
    '\L_Fing5_A',
    '\L_Little_A',
    '\L_Little_A_1',
    'Sf1_\L',
    'L_FINGER51',
    'LittleFinger1\L',
    '\LFingerA1',
    'LittA_\L',
    'Pinky1_\L',
    '\Lf_Pinky1',
    'Pinky_01_\L',
    '\L_Finger_E1',
    'Little01_\L',
    'Arm_\L_Finger_5_1',
    '\L_Littlefinger_A',
    'PinkyA\LT_01',
    'J_Bip_\L_Little1',
    'Bip_FPinky00_\L',
    'Arm_\L_Finger_5a',
    'J_Ko_A_\L',
    '\LFinger5Proximal',
    'Mixamorig:\LHandPinky1',
]
bone_list['leftLittleMedial'] = [
    'LittleFinger2_\L',
    'Little2_\L',
    '\LPinky2',
    '\LPinky2N',
    '\LLittle2N',
    'F_Pinky_02_\L',
    '\L_Pinky1',
    '\L_Pinkey_02',
    '\LHandPinky2',
    '\LFinger41',
    'Finger5_3_\L',
    'H_\L_Pinky2',
    'Bip_Pinky_1_\L',
    'Bip_\L_Finger41',
    '\L_Fing5_B',
    '\L_Little_B',
    '\L_Little_B_1',
    'Sf2_\L',
    'L_FINGER52',
    'LittleFinger2\L',
    '\LFingerA2',
    'LittB_\L',
    'Pinky2_\L',
    '\Lf_Pinky2',
    'Pinky_02_\L',
    '\L_Finger_E2',
    'Little02_\L',
    'Arm_\L_Finger_5_2',
    '\L_Littlefinger_B',
    'PinkyB\LT_01',
    'J_Bip_\L_Little2',
    'Bip_FPinky01_\L',
    'Arm_\L_Finger_5b',
    'J_Ko_B_\L',
    '\LFinger5Medial',
    'Mixamorig:\LHandPinky2',
]
bone_list['leftLittleDistal'] = [
    'LittleFinger3_\L',
    'Little3_\L',
    '\LPinky3',
    '\LPinky3N',
    '\LLittle3N',
    'F_Pinky_03_\L',
    '\L_Pinky2',
    '\L_Pinkey_03',
    '\LHandPinky3',
    '\LFinger42',
    'Finger5_4_\L',
    'H_\L_Pinky3',
    'Bip_Pinky_2_\L',
    'Bip_\L_Finger42',
    '\L_Fing5_C',
    '\L_Little_C',
    '\L_Little_C_1',
    'Sf3_\L',
    'L_FINGER53',
    'LittleFinger3\L',
    '\LFingerA3',
    'LittC_\L',
    'Pinky3_\L',
    '\Lf_Pinky3',
    'Pinky_03_\L',
    '\L_Finger_E3',
    'Little03_\L',
    'Arm_\L_Finger_5_3',
    '\L_Littlefinger_C',
    'PinkyC\LT_01',
    'J_Bip_\L_Little3',
    'Bip_FPinky02_\L',
    'Arm_\L_Finger_5c',
    'J_Ko_C_\L',
    '\LFinger5Distal',
    'Mixamorig:\LHandPinky3',
]
