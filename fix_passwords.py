import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

print("=== Fixing User Passwords ===")

# List of users to update with new passwords
users_to_update = [
    {'username': 'danish', 'new_password': 'SecurePass123!'},
    {'username': 'haris', 'new_password': 'SecurePass456!'},
    # Add your test users here
]

for user_info in users_to_update:
    try:
        user = User.objects.get(username=user_info['username'])
        print(f"Updating {user.username}...")
        
        # Set new password with proper hashing
        user.set_password(user_info['new_password'])
        user.save()
        
        print(f"  ✓ Updated {user.username} with password: {user_info['new_password']}")
        print(f"  New hash: {user.password[:50]}...")
        
    except User.DoesNotExist:
        print(f"✗ User {user_info['username']} not found")

# Create a test user if needed
test_user, created = User.objects.get_or_create(
    username='testuser',
    defaults={'email': 'test@example.com'}
)
if created:
    test_user.set_password('TestPassword123!')
    test_user.save()
    print(f"\n✓ Created test user: testuser / TestPassword123!")

print("\n=== All Users ===")
for user in User.objects.all():
    print(f"  {user.username}: {user.password[:20]}...")
