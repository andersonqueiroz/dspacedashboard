from django.contrib import admin

from dspacedashboard.autopermission.models import AutoPermissionUser

@admin.register(AutoPermissionUser)
class DepartmentAdmin(admin.ModelAdmin):
	list_display = ('netid', 'created', 'created_at')
	search_fields = ('netid', )
	actions = ('update_dspace_users',)

	@admin.action(description='Atualizar usuários selecionados no DSpace')
	def update_dspace_users(self, request, queryset):
		success = 0
		errors = 0
		for user in queryset:
			user.update_dspace_user()
			if user.created:
				success += 1
			else:
				errors += 1
		self.message_user(
			request,
			f'{success} usuário(s) atualizado(s) com sucesso. {errors} com erro.'
		)