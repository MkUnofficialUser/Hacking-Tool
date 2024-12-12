�
    ��ZgQ  �                   ��  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlm	Z	 d dl
mZmZmZ dZdZdZdZd	Zd
ZdZdZej,                  Zi ZdZdZdZdZdZdZdZedz   ez   dz   ez   dz   ez   Z edz   ez   dz   ez   dz   ez   Z!edz   ez   dz   ez   dz   ez   Z"edz   ez   dz   ez   dz   ez   Z#edz   ez   dz   ez   dz   ez   Z$edz   ez   dz   ez   dz   ez   Z%edz   ez   dz   ez   dz   ez   Z&edz   ez   dz   ez   dz   ez   Z'edz   ez   dz   ez   dz   ez   Z(edz   ez   d z   ez   dz   ez   Z)edz   ez   d!z   ez   dz   ez   Z*edz   ez   d"z   ez   d#z   d$z   Z+d%ez   d&z   ez   d'z   ez   d(z   ez   d)z   ez   d*z   ez   d%z   Z,d+� Z-d,� Z. ej^                  �       ja                  d-�      � d. ej^                  �       ja                  d/�      � �Z1d0� Z2d1� Z3d2� Z4d3� Z5d4� Z6d5� Z7d6� Z8d7� Z9d8� Z:d9� Z;d:� Z<d;� Z=d<� Z>d=� Z?d>� Z@d?� ZAd@� ZBdA� ZCdB� ZDdC� ZEdD� ZFdE� ZGdF� ZH edG�H�       eeeeeeeeeej�                  ej�                  ej�                  ej�                  ej�                  ej�                  ej�                  gZPdI� ZQe	ZRdJ� ZSdK� ZTeUdLk(  r eT�        yy)M�    N)�datetime)�logohelpmsg)�init�Fore�Stylez[0;31mz[0;32mz[0;34mz[0;95mz[0;36mz[0;37mz[0;93mz[0;90mz	error.logzupi_link.py ztransactions.txt zupi_qr_code.pngzusername.txtg     �u@g      9@z

[�1z] z
[�2�3�4�5�6�7�?u   √�X�!�+�]z Please Wait...�
z1 __  __   ____            __  __   _   _  __  __
z1|  \/  | |  _ \          |  \/  | | | | | \ \/ /
z1| |\/| | | |_) |  _____  | |\/| | | |_| |  \  / 
z1| |  | | |  _ <  |_____| | |  | | |  _  |  /  \ 
z/|_|  |_| |_| \_\         |_|  |_| |_| |_| /_/\_c                 �.   � t        j                  | �       y �N)�time�sleep)�secondss    �pg-program.py�	wait_timer   P   s   � ��J�J�w��    c                  �b   � t        j                  t         j                  dk(  rd�       y d�       y )N�posix�clear�cls)�os�system�name� r   r   �clear_displayr%   T   s   � ��I�I����G�+�g�7��7r   z%I:%M %pz & z%d/%m/%Yc                 �   � | dz   D ]T  }t         j                  j                  |�       t         j                  j                  �        t	        j
                  d�       �V y )Nr   g{�G�z�?)�sys�stdout�write�flushr   r   )�n�words     r   �	slowprintr-   Z   s>   � ��D����
�
������
�
�����
�
�4�� r   c                  �  � 	 t        j                  �       } t        t        d�      5 }|j	                  | �       d d d �       y # 1 sw Y   y xY w# t
        $ r1}t        t        � |� ��       t        t        |�      �       Y d }~y d }~ww xY w)N�w)
r!   �getlogin�open�username_pathr)   �	Exception�print�error�	log_error�str)�username�file�es      r   �save_usernamer;   `   sd   � ���;�;�=���-��%���J�J�x� � &�%�%��� �����s�m���#�a�&�����s3   �$A �A�A �A
�A �
A �	B�'B�Bc                  �~  � 	 t        t        d�      5 } | j                  �       j                  �       }d d d �       t	        t
        dz   t
        z   dz   t        j                  z   �      j                  �       }|k(  rt        t        dz   �       y t        t        dz   �       t        t        �       y # 1 sw Y   �~xY w# t        $ rA}t        t        t        z   dz   t        z   dz   �       t!        t#        |�      �       Y d }~y d }~wt$        $ r1}t        t        � |� ��       t!        t#        |�      �       Y d }~y d }~ww xY w)N�rzEnter Your Secret Key Here
�: z!Your Secret Key Has Been Verifiedz%Your Secret Key Has Not Been Verified�File Not Found.
�Make Sure All Files Are There)r1   r2   �read�strip�input�askr   �	RESET_ALLr4   �successr5   � remove_all_files_and_directories�	directory�FileNotFoundError�transactions�advicer6   r7   r3   )r9   �saved_username�
user_inputr:   s       r   �verify_usernamerN   i   s�   � ���-��%��!�Y�Y�[�.�.�0�N� &� �3�=�=��C�d�J�U�_�_�\�]�c�c�e�
���'��'�=�=�>��%�?�?�@�,�Y�7� &�%�� � ��e�l�"�%8�8��?�@_�_�`��#�a�&����� �����s�m���#�a�&�����s@   �B: �B.�AB: �!B: �.B7�3B: �:	D<�7C?�?D<�'D7�7D<c                  �   � t        t        �       t        d�       t        �        t        t        �       t        �        t        �        y )N�      @)r-   �pwr   r%   �	logomrmhxr;   rN   r$   r   r   �username_authenticationrS   |   s(   � ��b�M��d�O��O��i���O��r   c                 �  � t        j                  | �      D ]�  }t         j                  j                  | |�      }t         j                  j	                  |�      rK	 t        j
                  |�       t        t        j                  dz   t        j                  z   d|� d�z   �       ��t         j                  j                  |�      s��	 t        j                  |�       t        t        j                  dz   t        j                  z   d|� d�z   �       �� y # t        $ rp}t        t        j                  dz   t        j                  z   d|� d�z   �       t        t        j                  dz   t        j                  z   |� z   �       Y d }~��nd }~ww xY w# t        $ rp}t        t        j                  dz   t        j                  z   d|� d�z   �       t        t        j                  dz   t        j                  z   |� z   �       Y d }~���d }~ww xY w)Nu   [✓]zFile z Removed Successfully.
u   [×]zError Removing Directory z ! 
z
Directory )r!   �listdir�path�join�isfile�remover4   r   �CYAN�GREEN�OSError�RED�isdir�shutil�rmtree)rH   �item�	item_pathr:   s       r   rG   rG   �   s�  � ��
�
�9�%���G�G�L�L��D�1�	��7�7�>�>�)�$�>��	�	�)�$��d�i�i�'�)�D�J�J�6�5���F^�9_�_�`� �W�W�]�]�9�%�>����i�(��d�i�i�'�)�D�J�J�6�:�d�V�Kc�9d�d�e� &�� � >��d�i�i�&�(�4�8�8�3�8Q�RV�QW�W\�6]�]�^��d�i�i�&�(�4�8�8�3���<�=�=��>�� � >��d�i�i�&�(�4�8�8�3�8Q�RV�QW�W\�6]�]�^��d�i�i�&�(�4�8�8�3���<�=�=��>�s4   �A	D�A	F�	F	�A%F�F	�	H�A%H � Hc                  �6  � t        t        �       t        d�       t        �        t        t        �       t        t        dz   �       t        t        dz   �       t        t        dz   �       t        t        dz   t        z   dz   t        j                  z   �      } | dk(  rt        �        y | dk(  rHt        t        �       t        d�       t        �        t        t        �       t        j                  �        y t        t        d	z   t         z   d
z   �       t#        �        y )NrP   z(Would You Like To Proceed With Payment ?zYes, Go Ahead.zNo, Go Back.�Enter Your Choice
r>   r   r	   �Invalid Choice.
�Please Try Again.)r-   rQ   r   r%   rR   r4   rD   �num01�num02rC   r   rE   �select_residentr'   �exitr5   rK   �ask_for_payment��choices    r   rk   rk   �   s�   � ��b�M��d�O��O��i��	�#�8�
8�9�	�%� �
 �!�	�%��
���3�.�.��4�t�;�e�o�o�M�N�F���}���	�3���"���$�����)�����
��e�'�'��.�/B�B�C��r   c                  ��  � t        t        �       t        d�       t        �        t        t        �       t        t        dz   t        j                  z   �       t        t        dz   �       t        t        dz   �       t        t        dz   t        z   dz   t        j                  z   �      } | dk(  rt        �        y | dk(  rt        �        y t        t        d	z   t        z   d
z   �       t!        �        y )NrP   �Select Your ChoicezIndian ResidentzNon-Indian Residentrd   r>   r   r	   re   rf   )r-   rQ   r   r%   rR   r4   rD   r   rE   rg   rh   rC   �indian_resident�non_indian_residentr5   rK   ri   rl   s    r   ri   ri   �   s�   � ��b�M��d�O��O��i��	�#�"�
"�U�_�_�
4�5�	�%�!�
!�"�	�%�%�
%�&��3�,�,�s�2�T�9�E�O�O�K�L�F���}���	�3�����e�'�'��.�/B�B�C��r   c                  �&  � t        t        �       t        d�       t        �        t        t        �       t        t        dz   t        j                  z   �       t        t        dz   �       t        t        dz   �       t        t        dz   t        z   dz   t        j                  z   �      } | dk(  rt        t        dz   �       t        �        y | d	k(  rt        t        d
z   �       t        �        y t        t        dz   t         z   dz   �       t#        �        y )NrP   ro   zUPI PaymentzOther Optionsrd   r>   r   zOpening UPI Payment...r	   zOpening Other Options...re   rf   )r-   rQ   r   r%   rR   r4   rD   r   rE   rg   rh   rC   rF   �upi_paymentrq   r5   rK   ri   rl   s    r   rp   rp   �   s�   � ��b�M��d�O��O��i��	�#�"�
"�U�_�_�
4�5�	�%��
��	�%��
� ��3�,�,�s�2�T�9�E�O�O�K�L�F���}��g�.�.�/���	�3���g�0�0�1����e�'�'��.�/B�B�C��r   c                  �R  � t        t        �       t        d�       t        �        t        t        �       t        t        dz   t        j                  z   �       t        t        dz   �       t        t        dz   �       t        t        dz   t        z   dz   t        j                  z   �      } | dk(  r(t        t        dz   �       t        j                  d	�       y | d
k(  r(t        t        dz   �       t        j                  d�       y t        t        dz   t         z   dz   �       t#        �        y )NrP   ro   zKo-Fi�PayPalrd   r>   r   zOpening Ko-Fi...z*xdg-open https://ko-fi.com/mrmayankhackerxr	   zOpening PayPal...z9xdg-open https://www.paypal.com/ncp/payment/4MFMYUBPQQ36Yre   rf   )r-   rQ   r   r%   rR   r4   rD   r   rE   rg   rh   rC   rF   r!   r"   r5   rK   ri   rl   s    r   rq   rq   �   s�   � ��b�M��d�O��O��i��	�#�"�
"�U�_�_�
4�5�	�%��-��	�%��.���3�,�,�s�2�T�9�E�O�O�K�L�F���}��g�(�(�)�
�	�	�>�?�	�3���g�)�)�*�
�	�	�M�N��e�'�'��.�/B�B�C��r   c                 �  � 	 t        t        d�      5 }|j                  t        � d| d�d|d�d|d�d|� d�
�       ddd�       y# 1 sw Y   yxY w# t        $ r1}t        t        � |� ��       t        t        |�      �       Y d}~yd}~ww xY w)	z Logs Payment Details In log.txt.r/   u   
Entered Amount: ₹�.2fu   
Refund Charges: ₹u   
Total Paid: ₹z	
Status: �

N)	r1   rJ   r)   �formatted_time_dater3   r4   r5   r6   r7   )�entered_amount�refund_charges�total_amount�statusr9   r:   s         r   �log_paymentr~   �   s�   � ���,��$���J�J�&�'� (&�&4�S�%9� :&�&4�S�%9� :"�".�s�!3� 4�!�(�$�	(�� %�$�$�� � �����s�m���#�a�&�����s3   �A �(A�A �A�A �A �	B	�'B�B	c                 �   � 	 t        t        d�      5 }|j                  t        � d| � d��       ddd�       y# 1 sw Y   yxY w# t        $ r1}t        t        � |� ��       t        t        |�      �       Y d}~yd}~ww xY w)zLogs Errors In error.log.�az

 Error : rx   N)	r1   �
error_filer)   ry   r3   r4   r5   r6   r7   )�error_messager9   r:   s      r   r6   r6   �   sl   � ���*�c�"�d��J�J�&�'�}�]�O�4�H�� #�"�"�� � �����s�m���#�a�&�����s0   �A �7�A �A �A � A �	A=�'A8�8A=c                  �F  � t        t        �       t        d�       t        �        t        t        �       	 t        t        dz   t        z   dz   �       t        t        dz   t        z   dz   t        j                  z   �      j                  �       } | st        n
t        | �      }|t        k  rt        t        dz   �       	 t        �        y|t         z   }dt#        j$                  �       � �}d	|d
�d|� d�}|t&        d<   t)        |t         |d�       t        �        y# t*        $ r:}t        t        dz   t        z   dz   �       t-        t/        |�      �       Y d}~�Id}~wt0        $ r1}t        t        � |� ��       t-        t/        |�      �       Y d}~��d}~ww xY w# t        �        w xY w)z Function To Process UPI Payment.rP   u   Minimum Amount Is ₹350.
u0   Default Amount ₹350 Will Be Used If Left BlankzPlease Enter The Amount
r>   u"   Amount Cannot Be Less Than ₹350.NzPayment From zJ upi://pay?pa=501026852229@NSPB0000002.ifsc.npci&pn=MR MAYANK HACKER X&am=rw   z&tn=z&cu=INR�MRMHXz	Pending !�Invalid Input.
�Please Enter A Number.)r-   rQ   r   r%   rR   r4   rK   rC   rD   r   rE   rB   �DEFAULT_AMOUNT�floatr5   �check_user_environment�REFUND_CHARGES�getpass�getuser�upi_link_datar~   �
ValueErrorr6   r7   r3   )rM   �amountr|   �custom_message�upi_linkr:   s         r   rs   rs      sm  � ��b�M��d�O��O��i��!��f�2�2�6�9�:l�l�m��3�:�:�S�@�4�G�%�/�/�Y�Z�`�`�b�
�'1��u�Z�7H���N�"��%�<�<�=��" 	� �! ��.��(����):�(;�<��_�`l�mp�_q�qu�  wE�  vF�  FM�  N��!)��g���F�N�L�+�F� 	� �� � ��e�&�&�v�-�.F�F�G��#�a�&����� �����s�m���#�a�&������ 	� �sC   �BD �AD �	F�0E�F �F� 'F�F �F�F �F c                  �B  � t        t        �       t        d�       t        �        t        t        �       t        t        dz   �       t        t        dz   �       t        t        dz   �       t        t        dz   t        z   dz   t        j                  z   �      } | dk(  rNt        t        dz   �       t        j                  d	�       t        t        d
z   t        z   dz   �       t!        �        y | dk(  rt#        �        y t        t$        dz   t        z   dz   �       t'        �        y )NrP   z'Was The Payment Processed Successfully?zYes, Payment Processed.zNo, Payment Not Processedrd   r>   r   zProcessing your payment...�   zThank You For Your Payment.
z"Your Order Will Be Processed Soon.r	   re   rf   )r-   rQ   r   r%   rR   r4   rD   rg   rh   rC   r   rE   rK   r   r   rF   rS   �cancel_retryr5   �payment_confirmationrl   s    r   r�   r�      s�   � ��b�M��d�O��O��i��	�#�7�
7�8�	�%�)�
)�*�	�%�+�
+�,��3�,�,�s�2�T�9�E�O�O�K�L�F���}��f�1�1�2��
�
�1���g�5�5�f�<�=a�a�b��!�	�3�����e�'�'��.�/B�B�C��r   c                  �  � t        t        �       t        d�       t        �        t        t        �       t        t        dz   �       t        t        dz   �       t        t        dz   �       t        t        dz   t        z   dz   t        j                  z   �      } | dk(  rt        �        y | dk(  r1t        t        d	z   t        z   d
z   �       t        j                   �        y t        t"        dz   t        z   dz   �       t%        �        y )NrP   z>Would You Like To Retry The Payment Or Cancel The Transaction?zYes, Retry The Payment.zNo, Cancel The Payment.zEnter your choice
r>   r   r	   zTransaction Cancelled.
z
Thank You!re   rf   )r-   rQ   r   r%   rR   r4   rD   rg   rh   rC   r   rE   ri   rK   rF   r'   rj   r5   r�   rl   s    r   r�   r�   4  s�   � ��b�M��d�O��O��i��	�#�N�
N�O�	�%�)�
)�*�	�%�)�
)�*��3�,�,�s�2�T�9�E�O�O�K�L�F���}���	�3���f�/�/��7��D�E����
��e�'�'��.�/B�B�C��r   c                  ��   � dt         v rMt        j                  �       } | j                  t         d   �       | j	                  �        | j                  �        yt        t        dz   �       y)z-Generate And Display QR Code In The Terminal.r�   �,There Is No Data Available In The DictionaryN)r�   �qrcode�QRCode�add_data�make�print_asciir4   r5   )�qrs    r   �generate_qr_terminalr�   G  sI   � ��-���]�]�_��
���M�'�*�+�
���	� 	�����e�B�B�Cr   c                 �<  � dt         v r�t        j                  t         d   �      }|j                  | �       t	        t
        � d| � ��       t	        t
        dz   �       t	        t        dz   �       t        t        dz   �       t        �        yt	        t        dz   �       y)z&Generate And Save QR Code As An Image.r�   zQR Code Saved As: zQR Code Successfully Downloadedz$You Can Make Payments By Scanning It�Press Enter To Continue...r�   N)
r�   r�   r�   �saver4   rF   rK   rC   r�   r5   )�upi_qr_pathr�   s     r   �save_qr_imager�   T  s}   � ��-���[�[��w�/�0�� 	�������	�+�K�=�9�:��g�7�7�8��f�;�;�<��f�1�1�2����e�B�B�Cr   c                  ��   � dt         v rLt        t        dz   t        z   dz   �       t	        j
                  dt         d   � d��       t        t        �       yt        t        dz   �       y)zMobile users ke liye function.r�   zYou Are Using A Mobile Device.
zRunning Mobile User Function.z
xdg-open '�'r�   N)	r�   r4   rF   rK   r!   r"   r�   r�   r5   r$   r   r   �mobile_userr�   c  sX   � ��-���g�:�:�V�C�Fe�e�f� 	�	�	�J�}�W�5�6�a�8�9� 	�k�"��e�B�B�Cr   c                  �   � dt         v r6t        t        dz   t        z   dz   �       t	        �        t        t        �       yt        t        dz   �       y)zDesktop users ke liye function.r�   z You Are Using A Desktop Device.
zRunning Desktop User Function.r�   N)r�   r4   rF   rK   r�   r�   r�   r5   r$   r   r   �desktop_userr�   p  sC   � ��-���g�;�;�f�D�Gg�g�h� 	�� 	�k�"��e�B�B�Cr   c                 �j  � t        t        �       t        d�       t        �        t        t        �       t        t        � dt        � | � d��       t        t        dz   �       t        t        dz   �       	 t        t        t        dz   t        z   dz   t        j                  z   �      j                  �       �      }|dk(  r<t        t        d	z   t        z   d
z   �       | dk(  rt!        �        y| dk(  rut#        �        y|dk(  r<t        t$        dz   t        z   dz   �       | dk(  rt#        �        y| dk(  r3t!        �        yt        t$        dz   t        z   dz   �       t'        | �       yyy# t(        $ rE}t        t$        dz   t        z   dz   �       t+        t-        |�      �       t'        | �       Y d}~yd}~ww xY w)z�
    User se confirmation lene ke baad sahi function ko run karne ka kaam karta hai.
    Agar user ka confirmation galat ho, toh opposite function call hota hai.
    rP   zIs Your Detected Device
z	 Correct?zYes, This Device Is Correct.zNo, This Device Is Incorrect.rd   r>   �   zDevice Confirmed.
z"Proceeding With Detected Function.�Mobile Device�Desktop Devicer�   zDevice Confirmation Failed.
zRunning Opposite Function.r�   zPlease Enter 1 Or 2.r�   N)r-   rQ   r   r%   rR   r4   rD   rK   rg   rh   �intrC   r   rE   rB   rF   r�   r�   r5   �confirm_device_before_actionr�   r6   r7   )�detected_device�confirmationr:   s      r   r�   r�   }  sq  � �
 �b�M��d�O��O��i��	�S�E�*�6�(�?�2C�9�
M�N�	�%�.�
.�/�	�%�/�
/�0�6��5��%:�!:�S�!@�4�!G�%�/�/�!Y�Z�`�`�b�c���1���'�/�/��6�7[�[�\��/�1��� �$4�4����Q���%�7�7��>�?[�[�\��/�1��� �$4�4����%�*�*�6�1�2H�H�I�(��9�	 5� 5�� � 6��e�&�&�v�-�.F�F�G��#�a�&��$�_�5�5��6�s1   �4A4E$ �)E$ �90E$ �*E$ �:'E$ �$	F2�-;F-�-F2c                  ��   � t        j                  �       } d}| dv r&dt        j                  �       j                  v rd}nd}n| dk(  rd}nt	        t
        dz   �       y|rt        |�       yy)zr
    User ke device ka environment check karta hai aur confirmation lene ke baad sahi function run karta hai.
    N)�Linux�Darwin�Androidr�   r�   �Windowsz)Unable To Determine The User Environment.)�platformr"   �uname�releaser4   r5   r�   )�system_platformr�   s     r   r�   r�   �  sm   � �
 �o�o�'�O��O��-�-�����(�0�0�0�-�O�.�O�	�I�	%�*���e�?�?�@�� �$�_�5� r   c                  �6  � 	 t        t        d�      5 } | j                  �       }t        d�       t        |�       ddd�       y# 1 sw Y   yxY w# t        $ rA}t        t
        t        z   dz   t        z   dz   �       t        t        |�      �       Y d}~yd}~ww xY w)zZ
    This Function Reads The Content Of log.txt File And Displays It On The Terminal.
    r=   z
--- Transaction Details ---
Nr?   r@   )	r1   rJ   rA   r4   rI   r5   rK   r6   r7   )r9   �contentr:   s      r   �ReadLogFiler�   �  sx   � ���,��$���i�i�k�G��3�4��'�N� %�$�$�� � ��e�l�"�%8�8��?�@_�_�`��#�a�&�����s3   �A �'A�A �A�A �A �	B�7B�Bc                  �<  � 	 t        t        d�      5 } | j                  �       }t        d�       t        |�       ddd�       t	        t
        dz   t
        z   dz   t        j                  z   �      j                  �       }t        t        d�      5 } | j                  |�       t        t        dz   �       ddd�       y# 1 sw Y   ��xY w# 1 sw Y   yxY w# t        $ rA}t        t        t        z   dz   t        z   d	z   �       t        t        |�      �       Y d}~yd}~ww xY w)
z@
    This Function Updates The Content Of upi_link.py File.
    r=   z
--- Your UPI Link ---
NzRegister Your New UPI Link
r>   r/   z'UPI Link Has Been Successfully Updated!r?   r@   )r1   �upi_link_filerA   r4   rC   rD   r   rE   rB   r)   rF   rI   r5   rK   r6   r7   )r9   �current_content�new_contentr:   s       r   �UpdateUpiFiler�   �  s�   � ���-��%��"�i�i�k�O��-�.��/�"� &� �C� >�>��D�t�K�e�o�o�]�^�d�d�f�� �-��%���J�J�{�#��'�C�C�D� &�%� &�%�� &�%�� � ��e�m�#�&9�9�&�@�A`�`�a��#�a�&�����sL   �C �'B9�AC �$C�0C �9C�>C �C�
C �C �	D�7D�Dc                  �(  � t        t        dz   t        j                  z   �       t        t        dz   �       t        t
        dz   �       	 t        t        dz   t        z   dz   t        j                  z   �      } | dk(  rt        �        t        t        dz   �       y| dk(  rt        �        t        t        dz   �       yt        t        d	z   t        z   d
z   �       y# t        $ r1}t        t        � |� ��       t        t        |�      �       Y d}~yd}~ww xY w)z@
    The Main Menu Provides Options For The User To Choose.
    ro   zView Transaction Details.zUpdate The upi_link.py File.rd   r>   r   r�   r	   zInvalid Option.
rf   N)r4   rD   r   rE   rg   rh   rC   r�   rK   r�   r5   r3   r6   r7   )rm   r:   s     r   �X25_Functionr�   �  s�   � � 
�#�"�
"�U�_�_�
4�5�	�%�+�
+�,�	�%�.�
.�/���s�0�0�3�6��=����O�P���S�=��M��&�5�5�6��s�]��O��&�5�5�6��%�+�+�f�4�7J�J�K��� �����s�m���#�a�&�����s%   �	AC �!C �:C �	D� 'D�DF)�	autoresetc                 �|   � | j                  �       }|D ]'  }t        t        j                  t        �      |z   �       �) y r   )�
splitlinesr4   �randomrm   �colors)�text�lines�lines      r   �print_colored_textr�   �  s0   � ��O�O��E� ���f�m�m�F�#�d�*�+� r   c                  ��  � t        t        �       t        d�       t        �        t        t        �       t        t        dz   t        j                  z   �       t        t        dz   t        j                  z   �       t        t        dz   t        j                  z   �       t        t        dz   t        j                  z   �       t        t        dz   t        j                  z   �       t        t        dz   t        j                  z   �       t        t        dz   t        j                  z   �       t        t        d	z   t        j                  z   �       t!        t        d
z   t        z   dz   t        j                  z   �      } | dk(  r2t#        j$                  d�       t!        t&        dz   �       t)        �        y | dk(  r2t#        j$                  d�       t!        t&        dz   �       t)        �        y | dk(  r2t#        j$                  d�       t!        t&        dz   �       t)        �        y | dk(  r2t#        j$                  d�       t!        t&        dz   �       t)        �        y | dk(  r2t#        j$                  d�       t!        t&        dz   �       t)        �        y | dk(  rt+        �        y | dk(  rHt        t        �       t        d�       t        �        t        t        �       t-        j.                  �        y y )NrP   ro   zContact ~ WhatsappzContact ~ TelegramzJoin ~ WhatsappzJoin ~ TelegramzFollow ~ GitHubzGo Back To MainzExit The Programrd   r>   r   z$xdg-open https://wa.me/+917804844135r�   r	   z xdg-open https://t.me/GouravUiker
   z9xdg-open https://chat.whatsapp.com/HTp3rkM8rRGLevVwFDW5wDr   z,xdg-open https://t.me/HTp3rkM8rRGLevVwFDW5wDr   z(xdg-open https://github.com/JosefNoniyarr   r   )r-   rQ   r   r%   rR   r4   rD   r   rE   rg   rh   �num03�num04�num05�num06�num07rC   r!   r"   rK   �contact_Join_Follow�mainr'   rj   )�contacts    r   r�   r�     s�  � ��b�M��d�O��O��i��	�#�"�
"�U�_�_�
4�5�	�%�$�
$�u���
6�7�	�%�$�
$�u���
6�7�	�%�!�
!�E�O�O�
3�4�	�%�!�
!�E�O�O�
3�4�	�%�!�
!�E�O�O�
3�4�	�%�!�
!�E�O�O�
3�4�	�%�"�
"�U�_�_�
4�5��C�-�-�c�1�4�7�%�/�/�I�J�G��#�~�
�	�	�8�9��f�1�1�2���	�C��
�	�	�4�5��f�1�1�2���	�C��
�	�	�M�N��f�1�1�2���	�C��
�	�	�@�A��f�1�1�2���	�C��
�	�	�<�=��f�1�1�2���	�C����	�C���"���$�����)�����
� 
r   c                  ��  � 	 t        t        �       t        d�       t        �        t        t        �       t        t        dz   t        j                  z   �       t        t        dz   �       t        t        dz   �       t        t        dz   �       t        t        dz   �       t        t        dz   t        z   dz   t        j                  z   �      } | d	k(  rt        �        �n| d
k(  r`t        t        �       t        d�       t        �        t        t        �       t        d�       t        t         �       t        t"        dz   �       n�| dk(  rt%        �        n�| dk(  rHt        t        �       t        d�       t        �        t        t        �       t'        j(                  �        nB| dk(  r=t        t        �       t        d�       t        �        t        t        �       t+        �        ���)NrP   ro   zStart The ProgramzI Need Help�Contact�Exitrd   r>   r   r	   r�   r
   r   �X25)r-   rQ   r   r%   rR   r4   rD   r   rE   rg   rh   r�   r�   rC   rk   r�   r�   rK   r�   r'   rj   r�   rl   s    r   r�   r�   3  s>  � �
��"���$�����)���c�&�&����8�9��e�'�'�(��e�M�!�"��e�I�o���e�F�l���s�0�0�3�6��=����O�P���S�=����s�]��b�M��d�O��O��i� ��d�O��t�$��&�5�5�6��s�]��!��s�]��b�M��d�O��O��i� ��H�H�J��u�_��b�M��d�O��O��i� ��N�G r   �__main__)Vr!   r'   r   r�   r�   r�   r�   r   �helpmsgr   �coloramar   r   r   �red�green�blue�purple�cyan�white�yellow�grayrE   �reset_colourr�   r�   r�   rJ   r�   r2   r�   r�   rg   rh   r�   r�   r�   r�   r�   rD   rF   r5   rK   rQ   rR   r   r%   �now�strftimery   r-   r;   rN   rS   rG   rk   ri   rp   rq   r~   r6   rs   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r]   r[   �YELLOW�BLUE�MAGENTArZ   �WHITEr�   r�   r�   r�   r�   �__name__r$   r   r   �<module>r�      s  ��" 
� 
� � � � � � � � &� &� �������������������� �� �
���"������ ���� 	�w�����$�t�+�d�2�C�7���u��u��s�"�T�)�D�0�%�7���u��u��s�"�T�)�D�0�&�8���u��u��s�"�T�)�D�0�$�6���u��u��s�"�T�)�D�0�&�8���u��u��s�"�T�)�D�0�$�6���u��u��s�"�T�)�D�0�%�7��
�U�l�U��S� �4�'�$�.��6��
��,��
��
&��
-��
4�e�
;���u��u��s�"�T�)�D�0�#�5��	����	��	#�d�	*�T�	1�6�	9���5�L�5��3���%��+�,=�=���	�
�����	�� 	�	�
�� �	��	�
 	�	�

�� ����	��8� &�����0�0��<�=�S������AX�AX�Yc�Ad�@e�f� ����&�>�&�,�$�(�&�	�!�@�(�&
D�D�D�D�"6�H6�0��*�. �u� � �u�d�F�D�%���|�T�X�X�W[�Wa�Wa�cg�cn�cn�pt�py�py�{�  |H�  |H�  JN�  JS�  JS�  UY�  U_�  U_�  
`��,� ��)�X$�L �z���F� r   