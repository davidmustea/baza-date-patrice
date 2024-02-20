import os
import supabase

url = "https://tgwcszwdpjqtjpfpwici.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRnd2NzendkcGpxdGpwZnB3aWNpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDg0NTMwNTUsImV4cCI6MjAyNDAyOTA1NX0.cjLfWVaFISUk2-DKdfFV1R7Evv-zlqQDBbdVpl29QWo"
supabase = supabase.create_client(url, key)

response = supabase.table("furnizori").select("*").execute()
print(response)