from supabase import create_client


supabase_url = 'https://nvzeltqxchshgoxueiwo.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im52emVsdHF4Y2hzaGdveHVlaXdvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzYwMTI5NjQsImV4cCI6MjA1MTU4ODk2NH0.PEiNFfLBzPnQS_M_oGf6YFbip3zxybptfBeINYsWpc8'


def supa(name):
    supabase = create_client(supabase_url, supabase_key)
    while True:
        result = supabase.table('otp_data') \
            .select('otp, created_at') \
            .eq('name', name) \
            .order('created_at', desc=True) \
            .limit(1) \
            .execute()
        print(result)
        if result.data != []:
            break
    data = result.data[0]['otp']
    
    delete = supabase.table('otp_data') \
        .delete() \
        .eq('otp', data) \
        .execute()
    
    # if result.error:
    #     print(f"Error: {result.error}")
    #     return None
    
    return data
